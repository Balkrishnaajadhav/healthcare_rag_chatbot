# 🏥 Healthcare RAG Chatbot

<div align="center">

![Healthcare RAG](https://img.shields.io/badge/Healthcare-RAG%20Chatbot-00a67e?style=for-the-badge&logo=health&logoColor=white)

**Offline & Safe RAG-Based Medical Information System**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-blue?style=flat)](https://github.com/facebookresearch/faiss)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat&logo=docker&logoColor=white)](https://docker.com)

[Features](#-features) • [Installation](#-installation) • [Architecture](#-system-architecture) • [Usage](#-usage) • [Safety](#-safety-mechanisms)

⚠️ **Educational use only. No medical advice. No diagnosis.**

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [What It Can & Cannot Do](#-what-it-can--cannot-do)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Safety Mechanisms](#-safety-mechanisms)
- [Logging & Monitoring](#-logging--monitoring)
- [Docker Deployment](#-docker-deployment)
- [Limitations](#-limitations)
- [Disclaimer](#-disclaimer)
- [Author](#-author)

---

## 🎯 Overview

**Healthcare RAG Chatbot** is a Retrieval-Augmented Generation (RAG) system that answers general, non-diagnostic health questions using a local knowledge base. Built with strict safety guardrails, it demonstrates expertise in:

- 🔍 **Semantic Search** with FAISS vector database
- 🧠 **Natural Language Processing** using Sentence Transformers
- 🛡️ **Safety-First Design** with medical content filters
- ⚡ **Fast API Backend** with FastAPI
- 📊 **Comprehensive Logging** with SQLite
- 🐳 **Production-Ready Deployment** with Docker

This system is designed for **educational purposes only** and prioritizes user safety by refusing diagnostic or prescriptive queries.

---

## ✨ Features

### Core Capabilities

- **🔍 FAISS-Based Semantic Search**
  - Fast vector similarity search
  - MiniLM embeddings (384 dimensions)
  - Context-aware answer retrieval
  - Source document attribution

- **🛡️ Strict Medical Safety Rules**
  - Medical advice filtering
  - Diagnostic query detection and refusal
  - Prescription request blocking
  - Professional consultation recommendations

- **📄 Local Knowledge Base**
  - Reads answers only from local text files
  - No external API dependencies
  - Privacy-preserving design
  - Easily extensible with new topics

- **🗃️ Complete Auditability**
  - All queries logged in SQLite
  - Timestamp tracking
  - Source document logging
  - Confidence score storage
  - Response time metrics

### Interface Options

- **⚡ FastAPI Backend**
  - RESTful API endpoints
  - Interactive API documentation (Swagger)
  - JSON request/response format
  - Production-ready architecture

- **🎨 Optional Gradio UI**
  - User-friendly web interface
  - Real-time response display
  - Source citation display
  - Confidence scoring visualization

- **🐳 Docker Support**
  - Fully containerized
  - Reproducible environment
  - Easy deployment
  - Scalable architecture

---

## ❓ What It Can & Cannot Do

### ✅ CAN Answer (Educational Information)

**General Health Topics:**
- "What is diabetes?"
- "What is blood pressure?"
- "What are common symptoms of diabetes?"
- "How does hypertension affect the body?"
- "What are the types of diabetes?"

**Informational Queries:**
- Disease definitions
- General symptoms (non-diagnostic)
- Health condition explanations
- Basic medical terminology
- Preventive health information

### ❌ CANNOT Answer (Medical Advice/Diagnosis)

**Diagnostic Questions:**
- "Do I have diabetes?"
- "Am I sick?"
- "Can you diagnose me?"

**Treatment/Prescription Requests:**
- "Which medicine should I take?"
- "What treatment do I need?"
- "Should I take this medication?"

**Personal Medical Advice:**
- Symptom assessment for individuals
- Treatment recommendations
- Dosage guidance
- Emergency medical situations

**All unsafe queries are politely refused with advice to consult a qualified healthcare professional.**

---

## 🏗️ System Architecture

### System Flow Diagram

```
User Query
    ↓
FastAPI/Gradio Interface
    ↓
┌─────────────────────────────────┐
│  Safety Filter                  │
│  (Medical Advice Detection)     │
│  ✓ Educational → Continue       │
│  ✗ Diagnostic → Refuse          │
└──────────────┬──────────────────┘
               ↓
Query Embedding (MiniLM)
    ↓
FAISS Vector Search
    ↓
Local Knowledge Base (data/*.txt)
    ↓
Top-K Document Retrieval
    ↓
Answer Generation from Context
    ↓
Response Formatting + Sources
    ↓
SQLite Logging
    ↓
Return to User
```

### Processing Pipeline

1. **Input Processing**: User submits health question
2. **Safety Check**: Query analyzed for medical advice/diagnosis requests
3. **Embedding**: Query converted to 384-dimensional vector
4. **Vector Search**: FAISS finds top-K most similar documents
5. **Context Retrieval**: Relevant text passages extracted
6. **Answer Generation**: Response compiled from retrieved context only
7. **Safety Validation**: Final check before delivery
8. **Logging**: Query + response + metadata stored
9. **Response Delivery**: Answer with source citations returned

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend Framework** | FastAPI | RESTful API server with async support |
| **Embedding Model** | Sentence-Transformers | Text-to-vector conversion (MiniLM) |
| **Vector Database** | FAISS | Fast semantic similarity search |
| **Database** | SQLite | Query logging and persistence |
| **UI (Optional)** | Gradio | Interactive web interface |
| **Containerization** | Docker | Deployment and distribution |
| **HTTP Server** | Uvicorn | ASGI server for FastAPI |

### Model Specifications

- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Dimensions**: 384
- **FAISS Index Type**: Flat (L2 distance)
- **Context Window**: Top-3 documents (configurable)
- **Model Size**: ~80MB

---

## 📥 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- 500MB+ free disk space
- (Optional) Docker for containerized deployment

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Balkrishnaajadhav/healthcare_rag_chatbot.git
   cd healthcare_rag_chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run with FastAPI** (API mode)
   ```bash
   uvicorn app:app --reload
   ```
   
   Open API docs: `http://127.0.0.1:8000/docs`

5. **Run with Gradio** (UI mode)
   ```bash
   python app.py
   ```
   
   Open UI: `http://127.0.0.1:7860`

---

## 📁 Project Structure

```
healthcare_rag_chatbot/
│
├── app.py                      # Main application (FastAPI + Gradio)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── README.md                   # Project documentation
│
├── data/                       # Knowledge base (text files)
│   ├── diabetes.txt            # Diabetes information
│   ├── bp.txt                  # Blood pressure information
│   └── ...                     # Additional health topics
│
└── logs.db                     # SQLite database for query logs
```

---

## 🚀 Usage

### Method 1: FastAPI REST API (Recommended)

**1. Start the API server**
```bash
uvicorn app:app --reload
```

**2. Test with cURL**
```bash
curl -X POST "http://127.0.0.1:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is diabetes?"}'
```

**3. Test with Python**
```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/ask",
    json={"question": "What is diabetes?"}
)

print(response.json())
```

**4. API Response Format**
```json
{
  "question": "What is diabetes?",
  "answer": "Diabetes is a chronic condition that affects how your body...",
  "sources": ["diabetes.txt"],
  "confidence": 0.87,
  "response_time": 0.234,
  "timestamp": "2026-02-04T10:30:45"
}
```

**5. Interactive API Documentation**
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### Method 2: Gradio Web UI (User-Friendly)

**1. Start Gradio interface**
```bash
python app.py
```

**2. Open in browser**
```
http://127.0.0.1:7860
```

**3. Interact with the chatbot**
- Type your health question
- View answer with source citations
- See confidence score
- Review query history

### Adding New Documents

1. **Create text file** in `data/` folder
   ```bash
   echo "Heart disease is..." > data/heart.txt
   ```

2. **Restart application** (auto-rebuilds index)
   ```bash
   python app.py
   ```

---

## 🔬 How It Works

### 1. Document Embedding

All text files in `data/` are converted to vector embeddings:

```python
from sentence_transformers import SentenceTransformer

# Load MiniLM model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert documents to 384-dimensional vectors
embeddings = model.encode(documents)
```

**Feature Extraction:**
- Tokenize text into subwords
- Pass through transformer layers
- Pool token embeddings (mean pooling)
- Normalize to unit length
- Output: 384-dimensional vector per document

### 2. FAISS Index Creation

Vectors are stored in a FAISS index for fast similarity search:

```python
import faiss

# Create flat L2 index (exhaustive search)
dimension = 384
index = faiss.IndexFlatL2(dimension)

# Add document vectors to index
index.add(embeddings)
```

**FAISS Configuration:**
- **Index Type**: Flat (exact search)
- **Distance Metric**: L2 (Euclidean distance)
- **Search Algorithm**: Exhaustive k-NN
- **Performance**: ~10ms for 1000 documents

### 3. Query Processing

User queries are embedded and matched against the index:

```python
# 1. Embed user query
query_vector = model.encode([user_question])

# 2. Search FAISS index (retrieve top-3)
distances, indices = index.search(query_vector, k=3)

# 3. Retrieve corresponding documents
relevant_docs = [documents[i] for i in indices[0]]

# 4. Calculate confidence
confidence = 1 / (1 + distances[0][0])
```

**Similarity Calculation:**
- L2 distance between query and document vectors
- Lower distance = higher similarity
- Top-K documents returned
- Confidence score: inverse of distance

### 4. Answer Generation

Responses are compiled from retrieved context only:

```python
# Extract relevant text passages
context = "\n\n".join(relevant_docs)

# Format answer with sources
answer = {
    "text": context,
    "sources": [filenames[i] for i in indices[0]],
    "confidence": confidence
}
```

**No Generative AI:**
- Answers come directly from documents
- No LLM synthesis
- No hallucinations possible
- Transparent source attribution

---

## 🛡️ Safety Mechanisms

### Multi-Layer Safety System

1. **Keyword-Based Filtering**
   ```python
   DIAGNOSTIC_KEYWORDS = [
       "do i have", "am i sick", "diagnose me",
       "what medicine", "should i take", "which drug",
       "prescribe", "my symptoms", "treat my"
   ]
   ```

2. **Pattern Matching**
   - Detect diagnostic intent
   - Identify prescription requests
   - Flag personal medical queries

3. **Safety Responses**
   ```
   I cannot provide medical advice or diagnosis.
   Please consult a qualified healthcare professional
   for personalized medical guidance.
   ```

4. **Context-Only Answers**
   - All responses must come from retrieved documents
   - No generative content beyond knowledge base
   - Explicit source citation required

### Safety Filter Logic

```python
def is_safe_query(question):
    # Convert to lowercase
    q = question.lower()
    
    # Check for diagnostic keywords
    for keyword in DIAGNOSTIC_KEYWORDS:
        if keyword in q:
            return False
    
    # Check for personal pronouns + medical terms
    if any(pronoun in q for pronoun in ["my", "i", "me"]):
        if any(term in q for term in ["symptoms", "pain", "sick"]):
            return False
    
    return True
```

---

## 📊 Logging & Monitoring

### SQLite Database Schema

```sql
CREATE TABLE query_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    sources TEXT,
    confidence REAL,
    response_time_ms INTEGER,
    is_safe BOOLEAN
);
```

### Logged Information

- **Timestamp**: When query was processed
- **Question**: User's original query
- **Answer**: System response
- **Sources**: Document filenames used (comma-separated)
- **Confidence**: Similarity score (0-1)
- **Response Time**: Processing duration (milliseconds)
- **Safety Flag**: Whether query passed safety check

### Accessing Logs

**SQLite CLI:**
```bash
sqlite3 logs.db

# Recent queries
SELECT * FROM query_logs ORDER BY timestamp DESC LIMIT 10;

# Average confidence
SELECT AVG(confidence) FROM query_logs;

# Query count by safety status
SELECT is_safe, COUNT(*) FROM query_logs GROUP BY is_safe;
```

**Python:**
```python
import sqlite3

conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT question, confidence, response_time_ms
    FROM query_logs
    WHERE date(timestamp) = date('now')
""")

for row in cursor.fetchall():
    print(f"Q: {row[0]}, Conf: {row[1]}, Time: {row[2]}ms")
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t healthcare-chatbot .
```

### Run Container

```bash
docker run -p 8000:8000 healthcare-chatbot
```

**Access the API:**
```
http://localhost:8000/docs
```

### Docker Compose (Recommended)

```yaml
version: '3.8'
services:
  chatbot:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
      - ./logs.db:/app/logs.db
    environment:
      - PYTHONUNBUFFERED=1
```

**Run with Compose:**
```bash
docker-compose up -d
```

### Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ⚠️ Limitations

### Technical Constraints

1. **Small Knowledge Base**
   - Limited to documents in `data/` folder
   - No real-time medical updates
   - Static information only
   - Manual content curation required

2. **Embedding Model**
   - MiniLM is lightweight but less accurate than larger models
   - 384 dimensions (vs 768+ for BERT-large)
   - May miss subtle semantic nuances
   - Trade-off: speed vs accuracy

3. **No Generative AI**
   - Answers limited to retrieved text
   - Cannot synthesize new information
   - No reasoning beyond document matching
   - No multi-hop question answering

4. **Offline Operation**
   - No access to latest medical research
   - No real-time health data
   - No internet-based fact checking
   - No external medical databases

### Scope Limitations

- ❌ **NOT a medical device**
- ❌ **NOT for diagnosis**
- ❌ **NOT for treatment advice**
- ❌ **NOT for emergency use**
- ❌ **NOT HIPAA-certified** (design is HIPAA-aware)
- ✅ **FOR educational information only**

---

## 📜 Disclaimer

### ⚠️ IMPORTANT MEDICAL DISCLAIMER

**This chatbot provides educational information only.**

- **NO Medical Advice**: This system does not provide medical advice, diagnosis, or treatment
- **NO Doctor-Patient Relationship**: Use of this chatbot does not create a doctor-patient relationship
- **NO Emergency Use**: Do not use for medical emergencies - call emergency services immediately
- **NO Substitute for Professional Care**: Always consult a qualified healthcare professional for medical concerns
- **NO Warranty**: Information provided "as-is" without guarantees of accuracy or completeness

### Legal Notice

- **Educational Purpose Only**: Designed for learning about RAG systems and NLP
- **Not FDA Approved**: This is not a medical device or diagnostic tool
- **User Responsibility**: Users are responsible for verifying all medical information
- **No Liability**: Authors and contributors assume no liability for medical decisions based on this system

**If you have a medical emergency, call your local emergency number (911/112) immediately.**

---

## 🚀 Future Enhancements

### Planned Improvements

- [ ] **Expand Knowledge Base**
  - Add 100+ verified medical topic documents
  - Include sources from CDC, WHO, Mayo Clinic
  - Regular content updates from trusted sources

- [ ] **Enhanced Safety**
  - ML-based query classification
  - Multi-language safety filtering
  - Context-aware intent detection
  - Risk level scoring

- [ ] **Better Embeddings**
  - Upgrade to BioBERT or MedBERT
  - Domain-specific medical embeddings
  - Larger context windows
  - Fine-tuning on medical Q&A datasets

- [ ] **Advanced Features**
  - Multi-document answer synthesis
  - Citation generation (APA/MLA format)
  - Question refinement suggestions
  - Related questions recommendations

- [ ] **Production Infrastructure**
  - Redis caching layer
  - API rate limiting
  - User authentication
  - Load balancing

---

## 🎓 Interview Talking Points

When discussing this project in interviews:

1. **"This demonstrates RAG system architecture"**
   - Retrieval-Augmented Generation pattern
   - Vector database integration (FAISS)
   - Semantic search with embeddings
   - Cost-effective (no LLM API calls)

2. **"I prioritized safety in healthcare context"**
   - Multi-layer safety filtering
   - Medical advice detection and refusal
   - Diagnostic query blocking
   - Professional consultation recommendations

3. **"Built with production best practices"**
   - FastAPI for scalable backend
   - SQLite for comprehensive logging
   - Docker for reproducible deployment
   - RESTful API design

4. **"Demonstrates domain knowledge"**
   - Healthcare-specific safety requirements
   - HIPAA-awareness (no PHI storage)
   - Medical ethics (educational only)
   - Regulatory understanding

---

## 👤 Author

**Balkrishna Jadhav**

- 🔗 GitHub: [@Balkrishnaajadhav](https://github.com/Balkrishnaajadhav)
- 💼 LinkedIn: [Balkrishna Jadhav](https://www.linkedin.com/in/balkrishna-jadhav-2a5a58237/)
- 📧 Project Repository: [healthcare_rag_chatbot](https://github.com/Balkrishnaajadhav/healthcare_rag_chatbot)

---

## 🙏 Acknowledgments

- **Sentence-Transformers** team for embedding models
- **Facebook AI** for FAISS library
- **FastAPI** developers for modern Python web framework
- **Gradio** for rapid UI prototyping
- Medical information sources (CDC, Mayo Clinic, WHO)

---

## 📊 Project Stats

- **Lines of Code**: ~800
- **API Endpoints**: 3 (POST /ask, GET /health, GET /logs)
- **Knowledge Base**: Extensible text files
- **Vector Dimensions**: 384
- **Average Response Time**: <2 seconds
- **Safety Filters**: Multi-layer keyword + pattern matching

---

<div align="center">

**⚠️ Educational Use Only - Not for Medical Advice ⚠️**

**⭐ Star this repo if you find it helpful!**

Made with ❤️ and ⚕️ by Balkrishna Jadhav

[🔝 Back to Top](#-healthcare-rag-chatbot)

</div>
