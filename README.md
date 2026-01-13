🏥 𝗛𝗲𝗮𝗹𝘁𝗵𝗰𝗮𝗿𝗲 𝗥𝗔𝗚 𝗖𝗵𝗮𝘁𝗯𝗼𝘁 (𝗢𝗳𝗳𝗹𝗶𝗻𝗲 & 𝗦𝗮𝗳𝗲)

A Retrieval-Augmented Generation (RAG) based healthcare chatbot that answers general, non-diagnostic health questions using a local knowledge base.

⚠️ 𝗘𝗱𝘂𝗰𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝘂𝘀𝗲 𝗼𝗻𝗹𝘆. 𝗡𝗼 𝗺𝗲𝗱𝗶𝗰𝗮𝗹 𝗮𝗱𝘃𝗶𝗰𝗲. 𝗡𝗼 𝗱𝗶𝗮𝗴𝗻𝗼𝘀𝗶𝘀.

📌 𝗞𝗲𝘆 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀
✅ Fully offline (no external APIs)
📄 Reads answers only from local text files.
🛡️ Strict medical safety rules
🔍 FAISS-based semantic search
🧠 MiniLM embeddings
🗃️ All queries logged in SQLite
⚡ FastAPI backend
🎨 Optional Gradio UI
🐳 Docker-ready

❓ 𝗪𝗵𝗮𝘁 𝗜𝘁 𝗖𝗮𝗻 & 𝗖𝗮𝗻𝗻𝗼𝘁 𝗗𝗼

✅ 𝗖𝗔𝗡 𝗮𝗻𝘀𝘄𝗲𝗿
What is diabetes?
What is blood pressure?
What are common symptoms of diabetes?

❌ 𝗖𝗔𝗡𝗡𝗢𝗧 𝗮𝗻𝘀𝘄𝗲𝗿
Do I have diabetes?
Which medicine should I take?
Can you diagnose me?

Unsafe questions are politely refused with advice to consult a healthcare professional.

🧠 𝗦𝘆𝘀𝘁𝗲𝗺 𝗙𝗹𝗼𝘄 (𝗦𝗶𝗺𝗽𝗹𝗲)
1. Healthcare text files stored in `data/`
2. Text converted to embeddings (MiniLM)
3. Stored in FAISS vector index
4. User query embedded and matched
5. Answer generated only from retrieved text
6. Safety filter blocks medical advice
7. Query + response logged in SQLite

🗂️ 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲

healthcare_rag_chatbot/
│── app.py
│── requirements.txt
│── Dockerfile
│── README.md
│── data/
│   ├── diabetes.txt
│   ├── bp.txt
│── logs.db

⚙️ 𝗧𝗲𝗰𝗵 𝗦𝘁𝗮𝗰𝗸

* Python
* FastAPI
* Sentence Transformers (MiniLM)
* FAISS
* SQLite
* Gradio
* Docker

🚀 𝗥𝘂𝗻 𝗟𝗼𝗰𝗮𝗹𝗹𝘆 (𝗪𝗶𝘁𝗵𝗼𝘂𝘁 𝗗𝗼𝗰𝗸𝗲𝗿)
1️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start API
uvicorn app:app --reload

4️⃣ Open API docs
http://127.0.0.1:8000/docs
Use POST /ask to test.

🖥️ 𝗢𝗽𝘁𝗶𝗼𝗻𝗮𝗹 𝗚𝗿𝗮𝗱𝗶𝗼 𝗨𝗜
python app.py
Open: http://127.0.0.1:7860

🐳 𝗥𝘂𝗻 𝘄𝗶𝘁𝗵 𝗗𝗼𝗰𝗸𝗲𝗿
Build image
docker build -t healthcare-chatbot .
Run container
docker run -p 8000:8000 healthcare-chatbot
Open: http://127.0.0.1:8000/docs

📊 𝗟𝗼𝗴𝗴𝗶𝗻𝗴
All queries are stored in `logs.db` with:
* Timestamp
* User question
* Answer
* Retrieved sources
* Confidence score
* Response time

Ensures auditability and traceability.

⚠️ 𝗗𝗶𝘀𝗰𝗹𝗮𝗶𝗺𝗲𝗿
This chatbot provides educational information only.
It does not provide medical advice, diagnosis, or treatment.
Always consult a qualified healthcare professional.

🚧 𝗟𝗶𝗺𝗶𝘁𝗮𝘁𝗶𝗼𝗻𝘀
* Small local embedding model
* Limited to provided documents
* No real-time medical updates


👤 𝗔𝘂𝘁𝗵𝗼𝗿

𝗕𝗮𝗹𝗸𝗿𝗶𝘀𝗵𝗻𝗮 𝗝𝗮𝗱𝗵𝗮𝘃

🔗 𝗚𝗶𝘁𝗛𝘂𝗯:  https://github.com/Balkrishnaajadhav  
🔗 𝗟𝗶𝗻𝗸𝗲𝗱𝗜𝗻: https://https://www.linkedin.com/in/balkrishna-jadhav-2a5a58237/

