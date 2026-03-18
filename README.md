# 📚 AI Web Scraper & Book API — Crawl4AI + OpenAI + FastAPI

A simple **AI-powered web scraping and data service project** that extracts structured data from websites using **Crawl4AI** and **OpenAI LLMs**, and exposes the extracted data through a **FastAPI REST API**.

The scraper crawls a webpage, sends cleaned content to an LLM, extracts structured book data, and stores it as JSON.
The API layer then allows users to query the dataset, perform semantic search, or ask AI questions using a **RAG (Retrieval-Augmented Generation) pipeline**.

This project demonstrates how to combine **modern AI tools, web scraping, backend APIs, and semantic search** to build an intelligent data pipeline.

---

## 🚀 Features

* 🕸️ **Async Web Crawling** using Crawl4AI
* 🌐 **Browser Rendering** powered by Playwright
* 🤖 **AI Data Extraction** using OpenAI models
* 📦 **Structured Data Validation** with Pydantic
* 🔐 **Secure API Key Management** using python-dotenv
* 📄 Saves extracted data as **clean JSON dataset**
* ⚡ **REST API service** using FastAPI
* 🔎 **Search books by title**
* 🧠 **AI-powered Q&A endpoint** over full dataset
* 🔍 **RAG-based semantic search** using embeddings
* ⚖️ **Hybrid filtering** for structured queries (price conditions like `<`, `>`, `<=`, `>=`, `==`)

---

## 🧠 Architecture

```id="qos6q7"
Website
   ↓
Crawl4AI (Fetch + Clean HTML)
   ↓
Markdown Content
   ↓
OpenAI LLM
   ↓
Structured JSON
   ↓
Pydantic Validation
   ↓
books.json dataset
   ↓
Embeddings (Vector Store)
   ↓
Vector Search + Hybrid Filtering
   ↓
LLM Answer (RAG)
   ↓
FastAPI Service
```

---

## 📂 Project Structure

```id="8r1uyk"
crawl4ai-book-scraper
│
├── .env
├── main.py
├── api.py
├── requirements.txt
│
├── data/
│   └── books.json
│
├── scraper/
│   ├── crawler.py
│   └── schema.py
│
└── rag/
    ├── vector_store.py
    └── rag_pipeline.py
```

---

## ⚙️ Installation

Clone the repository and create a virtual environment.

```bash id="5r1z8l"
git clone <repo-url>
cd crawl4ai-book-scraper

python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash id="7th5ye"
pip install -r requirements.txt
playwright install chromium
```

---

## 🔑 Environment Variables

Create a `.env` file:

```id="q8u8rf"
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Scraper

Generate the dataset:

```bash id="eh4x9u"
python main.py
```

This will create:

```id="a0mp8x"
data/books.json
```

---

## ▶️ Run the API

Start the FastAPI server:

```bash id="d4v1sb"
uvicorn api:app --reload
```

Server will start at:

```id="6ttg61"
http://127.0.0.1:8000
```

Interactive API docs:

```id="8t2m6q"
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Get all books

```id="zq5qql"
GET /books
```

Returns the full dataset.

---

### Get book by title

```id="kj9h8z"
GET /books?title=Sapiens
```

Returns the matching book.

---

### Ask AI (Full Dataset)

```id="qis8i7"
GET /ask?question=Which books cost more than £50?
```

Uses the **entire dataset** for answering.

---

### Ask AI (RAG - Semantic Search)

```id="u2pxm6"
GET /ask-rag?question=Which books cost less than £50?
```

Uses:

* embeddings
* vector similarity search
* hybrid filtering (for price queries)

---

## 📄 Example Output

`data/books.json`

```json id="m6m2c7"
{
  "books": [
    {"title": "A Light in the Attic", "price": "£51.77"},
    {"title": "Tipping the Velvet", "price": "£53.74"}
  ]
}
```

---

## 🎯 Use Cases

* AI-powered web scraping
* Automated dataset generation
* LLM-assisted web data extraction
* Backend AI data services
* Semantic search systems
* Building datasets for **RAG / AI search engines**

---

## 📌 Notes

* Designed for **learning AI-based scraping + RAG pipelines**
* Uses a practice website:

https://books.toscrape.com

* Avoid scraping websites that prohibit automated access.

---

## 📜 License

MIT License
