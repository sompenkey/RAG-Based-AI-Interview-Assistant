# RAG-Based AI Interview Assistant

## Features
- Resume Upload
- RAG-based Question Generation
- FastAPI Backend
- Simple Frontend UI

## Run

pip install -r requirements.txt

set OPENAI_API_KEY=your_key  # Windows
export OPENAI_API_KEY=your_key  # Linux/Mac

uvicorn backend.main:app --reload

Open:
http://127.0.0.1:8000/docs