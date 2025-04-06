import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_and_process_document(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    chunks = text.split(". ")
    embeddings = model.encode(chunks, convert_to_tensor=True)
    return chunks, embeddings

def semantic_search(query, chunks, embeddings, top_k=3):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
    results = sorted(
        zip(chunks, scores), key=lambda x: x[1], reverse=True
    )[:top_k]
    return [
        {"text": chunk, "score": round(float(score), 4)}
        for chunk, score in results
    ]
