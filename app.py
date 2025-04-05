from flask import Flask, request, jsonify, render_template
from search_engine.processor import load_and_chunk_text
from search_engine.embedder import get_embeddings
from search_engine.searcher import build_faiss_index, search
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "frontend")
STATIC_DIR = os.path.join(TEMPLATE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

docs = load_and_chunk_text("data/sample.pdf")
doc_embeddings, model = get_embeddings(docs)
index = build_faiss_index(doc_embeddings)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def semantic_search():
    query = request.json.get("query")
    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = search(query, model, index, docs)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
