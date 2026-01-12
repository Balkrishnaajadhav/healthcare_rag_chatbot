from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import gradio as gr

import sqlite3
import time
import os
import sys
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from typing import List
safety_keywords = ["do i have", "should i take", "am i", "diagnose me"]




app = FastAPI(title="Healthcare RAG Chatbot")

def init_db():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS query_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            question TEXT,
            answer TEXT,
            sources TEXT,
            confidence REAL,
            latency REAL
        )
    """)

    conn.commit()
    conn.close()
    init_db()

def save_log(question, answer, sources, scores, latency):
    confidence = min(scores) if scores else None

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO query_logs (timestamp, question, answer, sources, confidence, latency)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        question,
        answer,
        ", ".join(sources),
        confidence,
        latency
    ))

    conn.commit()
    conn.close()



class QuestionRequest(BaseModel):
    question: str


class SearchResult(BaseModel):
    source: str
    text: str
    score: float


# Globals populated on startup
MODEL = None
INDEX = None
DOCUMENTS: List[str] = []
SOURCES: List[str] = []


def build_index(data_path: str = "data"):
    global MODEL, INDEX, DOCUMENTS, SOURCES
    MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    DOCUMENTS = []
    SOURCES = []

    if not os.path.isdir(data_path):
        raise FileNotFoundError(f"Data path not found: {data_path}")

    for filename in os.listdir(data_path):
        if filename.endswith(".txt"):
            with open(os.path.join(data_path, filename), "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    DOCUMENTS.append(text)
                    SOURCES.append(filename)

    if not DOCUMENTS:
        raise ValueError("No documents found in data/ to encode.")

    embeddings = MODEL.encode(DOCUMENTS, show_progress_bar=False, convert_to_numpy=True)
    if hasattr(embeddings, 'ndim') and embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    embeddings = np.asarray(embeddings).astype('float32')
    dimension = embeddings.shape[1]
    INDEX = faiss.IndexFlatL2(dimension)
    INDEX.add(embeddings)


@app.on_event("startup")
def on_startup():
    try:
        build_index()
        print("Index built. Files loaded:", SOURCES)
    except Exception as e:
        print(f"Startup error building index: {e}", file=sys.stderr)


@app.get("/health")
def health():
    return {"status": "ok", "documents": len(DOCUMENTS)}


@app.get("/search", response_model=List[SearchResult])
def search(q: str, k: int = 3):
    if MODEL is None or INDEX is None:
        raise HTTPException(status_code=503, detail="Model or index not ready")

    q_emb = MODEL.encode([q], convert_to_numpy=True)
    if q_emb.ndim == 1:
        q_emb = q_emb.reshape(1, -1)
    q_emb = np.asarray(q_emb).astype('float32')

    distances, indices = INDEX.search(q_emb, k)
    results: List[SearchResult] = []
    for dist, idx in zip(distances[0], indices[0]):
        results.append(SearchResult(source=SOURCES[int(idx)], text=DOCUMENTS[int(idx)], score=float(dist)))
    return results


@app.post("/ask")
def ask(req: QuestionRequest):
    q = req.question
    if is_medical_advice_question(q):
        return {
            "answer": "I cannot provide medical advice or diagnosis. Please consult a healthcare professional.",
            "sources": [],
            "scores": []
        }
    return generate_answer(q)


def is_medical_advice_question(question: str) -> bool:
    blocked_phrases = [
        "do i have",
        "should i take",
        "which medicine",
        "diagnosis",
        "can you diagnose",
        "treatment",
        "cure",
        "tablet",
        "medicine"
    ]
    question_lower = question.lower()
    return any(phrase in question_lower for phrase in blocked_phrases)


def search_documents(question: str, top_k: int = 3):
    q_emb = MODEL.encode([question], convert_to_numpy=True)
    if q_emb.ndim == 1:
        q_emb = q_emb.reshape(1, -1)
    q_emb = np.asarray(q_emb).astype('float32')
    distances, indices = INDEX.search(q_emb, top_k)
    results = []
    for i, idx in enumerate(indices[0]):
        results.append({
            "text": DOCUMENTS[idx],
            "source": SOURCES[idx],
            "score": float(distances[0][i])
        })
    return results


def generate_answer(question: str):
    if is_medical_advice_question(question):
        return {
            "answer": "I cannot provide medical advice or diagnosis. Please consult a healthcare professional.",
            "sources": [],
            "scores": []
        }

    results = search_documents(question)

    if not results:
        return {
            "answer": "Information not available in provided sources.",
            "sources": [],
            "scores": []
        }

    answer_text = "\n".join([r["text"] for r in results]).strip()
    used_sources = list({r["source"] for r in results})
    scores = [r["score"] for r in results]

    return {
        "answer": answer_text,
        "sources": used_sources,
        "scores": scores
    }


def gradio_chat(question):
    result = generate_answer(question)

    answer = result["answer"] + "\n\n⚠️ Disclaimer: This is educational information only."
    sources = ", ".join(result["sources"]) if result["sources"] else "N/A"
    scores = result["scores"]

    return answer, sources, scores

gradio_app = gr.Interface(
    fn=gradio_chat,
    inputs=gr.Textbox(label="Ask a healthcare question"),
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Textbox(label="Sources"),
        gr.JSON(label="Similarity Scores")
    ],
    title="Healthcare RAG Chatbot",
    description="Answers general healthcare questions using local files only. No medical advice."
)



if __name__ == "__main__":
    # Build index then launch Gradio UI
    try:
        build_index()
        print("Index built. Files loaded:", SOURCES)
    except Exception as e:
        print(f"Error building index: {e}", file=sys.stderr)
        sys.exit(1)

    gradio_app = gr.Interface(
        fn=gradio_chat,
        inputs=gr.Textbox(lines=2, placeholder="Ask a question"),
        outputs=[
            gr.Textbox(label="Answer"),
            gr.Textbox(label="Sources"),
            gr.Textbox(label="Scores")
        ],
        title="Healthcare RAG Chatbot",
    )

    gradio_app.launch()

if __name__ == "__main__":
    gradio_app.launch()
