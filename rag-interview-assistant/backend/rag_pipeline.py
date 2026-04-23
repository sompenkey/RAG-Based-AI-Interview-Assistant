from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.retriever import create_vectorstore, get_retriever
from backend.llm import get_llm


# Step 1: Chunking
def chunk_text(text):
    # ✅ Ensure text is string
    if not isinstance(text, str):
        try:
            text = str(text)
        except:
            raise ValueError("Invalid text format for chunking")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_text(text)


# Step 2: Build RAG
def build_rag_pipeline(text):
    chunks = chunk_text(text)

    db = create_vectorstore(chunks)
    retriever = get_retriever(db)
    llm = get_llm()

    return retriever, llm


# Step 3: Generate Questions (Manual RAG)
def generate_questions(rag):
    retriever, llm = rag

    query = "Generate interview questions from this resume"
    docs = retriever.invoke(query)

    if not docs:
        return "No resume data found."

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a professional interviewer.

    Resume:
    {context}

    Generate:
    1. 5 HR questions with answers
    2. 5 Technical questions with answers
    3. 5 Project-based questions with answers
    """

    try:
        response = llm.invoke(prompt)

        if hasattr(response, "content"):
            return response.content
        else:
            return str(response)

    except Exception as e:
        print("LLM ERROR:", str(e))
        return f"LLM Error: {str(e)}"