from sentence_transformers.util import cos_sim
import torch

def build_faiss_index(embeddings):
    return {"embeddings": embeddings}

def search(query, model, index, docs, top_k=5):
    query_embedding = model.encode([query], convert_to_tensor=True)
    doc_embeddings = index["embeddings"]
    scores = cos_sim(query_embedding, doc_embeddings)[0]

    top_k = min(top_k, len(scores))
    top_results = torch.topk(scores, k=top_k)

    results = []
    for score, idx in zip(top_results.values, top_results.indices):
        snippet = docs[idx].strip().replace("\n", " ")
        snippet = snippet[:400] + ("..." if len(snippet) > 400 else "")
        results.append({
            "document": snippet,
            "score": float(score)
        })
    return results
