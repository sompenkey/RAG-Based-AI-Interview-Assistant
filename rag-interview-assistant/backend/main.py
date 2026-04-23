from fastapi import FastAPI, UploadFile, File
from backend.utils import extract_text
from backend.rag_pipeline import build_rag_pipeline, generate_questions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

rag = None  # global variable

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    global rag

    try:
        text = extract_text(file.file)
        print("TEXT TYPE:", type(text))

        rag = build_rag_pipeline(text)

        return {"message": "Resume processed successfully"}

    except Exception as e:
        return {"error": str(e)}


@app.get("/questions/")
def get_questions():
    global rag

    if rag is None:
        return {"error": "Upload resume first"}

    try:
        result = generate_questions(rag)
        return {"result": result}

    except Exception as e:
        return {"error": str(e)}