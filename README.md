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
* ⚖️ **Hybrid filtering** for structured queries (`<`, `>`, `<=`, `>=`, `==`)
* 🐳 **Dockerized deployment** for easy setup

---

## 🧠 Architecture

```
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

```
crawl4ai-book-scraper
│
├── .env
├── main.py
├── api.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
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

## ⚙️ Installation (Local Setup)

```bash
git clone <repo-url>
cd crawl4ai-book-scraper

python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install chromium
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Scraper

Generate the dataset:

```bash
python main.py
```

This will create:

```
data/books.json
```

---

## ▶️ Run the API (Local)

```bash
uvicorn api:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

### Build & Start

```bash
docker compose up --build
```

### Access API

```
http://localhost:8000
http://localhost:8000/docs
```

---

## 📡 API Endpoints

### Get all books

```
GET /books
```

---

### Get book by title

```
GET /books?title=Sapiens
```

---

### Ask AI (Full Dataset)

```
GET /ask?question=Which books cost more than £50?
```

---

### Ask AI (RAG - Semantic Search)

```
GET /ask-rag?question=Which books cost less than £50?
```

Uses:

* embeddings
* vector search
* hybrid filtering

---

## 📄 Example Output

`data/books.json`

```json
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
* Backend AI services
* Semantic search systems
* Building datasets for **RAG / AI applications**

---

## 📌 Notes

* Designed for **learning AI + RAG pipelines**
* Uses practice website: https://books.toscrape.com
* Avoid scraping restricted websites

---

## 📜 License

MIT License
