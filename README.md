RAG-Based AI Interview Assistant (Resume Q&A Generator)

An AI-powered system that analyzes resumes and generates personalized technical and HR interview questions using Retrieval-Augmented Generation (RAG). The system simulates real interview scenarios by extracting relevant context from resumes and generating dynamic questions using LLMs.

---

## Features

- Upload and parse resumes (PDF/DOCX)
- Extract structured information from unstructured resume data
- Semantic search using vector embeddings
- Retrieval-Augmented Generation (RAG) pipeline
- AI-generated technical + HR interview questions
- Interactive chat-based interview simulation
- Role-based question generation (SDE, Data Analyst, etc.)

---

## System Architecture
Resume (PDF/DOCX)\
↓\
Text Extraction & Cleaning\
↓\
Chunking & Embedding Generation\
↓\
Vector Database (FAISS)\
↓\
Query + Context Retrieval\
↓\
LLM (GPT / HuggingFace Model)\
↓\
Generated Interview Questions & Answers


---

## Tech Stack

- **Programming Language:** Python  
- **NLP & ML:** Scikit-learn, NLTK  
- **Embeddings & RAG:** FAISS, LangChain / LlamaIndex  
- **LLM:** OpenAI / HuggingFace Models  
- **Backend:** FastAPI  
- **Data Handling:** Pandas, NumPy  

---

## Project Structure


rag-interview-assistant/ 
│ 
├── backend/ 
│ ├── main.py
│ ├── rag_pipeline.py
│ ├── retriever.py
│ ├── embeddings.py
│ ├── llm.py
│ └── utils.py
│
├── frontend/
│ ├── index.html
│ ├── script.js
│ └── style.css
│
├── requirements.txt
├── .gitignore
└── README.md
