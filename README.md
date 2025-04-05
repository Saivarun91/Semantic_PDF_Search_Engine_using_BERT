# 📚 Semantic PDF Search Engine using BERT

A lightweight and intuitive semantic search engine for PDF files powered by **Sentence-BERT** and **Flask**. You can search documents using natural language queries and get the most relevant sections, not just keyword matches.

---

## 🚀 Features

- 🔍 Semantic understanding using `all-MiniLM-L6-v2` (SBERT)
- 📄 Supports `.pdf` and `.txt` documents
- 🌐 Web interface using Flask + HTML/CSS/JS
- ⚡ Cosine similarity search over sentence embeddings
- 📦 Simple and easy to set up

---

## 🛠 Tech Stack

- Python
- Flask
- SentenceTransformers
- FAISS (for fast similarity search)
- PyMuPDF (PDF parsing)
- HTML, CSS, JavaScript

---

## 📁 Project Structure

semantic-search/ ├── app.py # Flask application entry point ├── requirements.txt # Python dependencies ├── data/ │ └── sample.pdf # PDF document to search ├── frontend/ │ ├── index.html # Frontend UI │ └── static/ │ └── styles.css # Basic styling ├── search_engine/ │ ├── processor.py # Loads and chunks text from PDF or TXT │ ├── embedder.py # Embeds the text using Sentence-BERT │ └── searcher.py # Performs semantic search with FAISS

---

## 🧪 Setup & Run Instructions

### 1. Clone the Repository
bash
git clone https://github.com/your-username/semantic-search.git
cd semantic-search


## Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Adding Your Content

1.  **Replace the default file:** Navigate to the `data` directory and replace the `sample.pdf` file (or `sample.txt` if that's the default) with your own PDF or `.txt` file.

2.  **Update filename in `app.py` (if necessary):** If you changed the filename from `sample.pdf` (or `sample.txt`), open the `app.py` file and locate the line where the file is loaded. Update the filename in the code to match your file's name. For example, if you named your file `my_document.pdf`, you would change the relevant line to reflect that.

## Running the Application

1.  **Execute the `app.py` script:**
    ```bash
    python app.py
    ```
    You should see output in your terminal indicating that the Flask development server is running.

## Accessing the Application

1.  **Open your web browser:** Go to the following address in your browser:
    ```
    http://localhost:5000
    ```

You should now be able to interact with your uploaded document through the web interface.