from flask import Flask, render_template, request
from search_engine.processor import load_and_process_document, semantic_search
from search_engine.utils import highlight_keywords

app = Flask(__name__)

# Load the document chunks and embeddings at startup
chunks, embeddings = load_and_process_document("data/sample.pdf")

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        query = request.form["query"]
        results = semantic_search(query, chunks, embeddings)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
