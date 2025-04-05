from sentence_transformers import SentenceTransformer

def get_embeddings(text_chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(text_chunks, convert_to_tensor=True)
    return embeddings, model
