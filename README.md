# 📚 AI Web Scraper & Book API — Crawl4AI + OpenAI + FastAPI

A simple **AI-powered web scraping and data service project** that extracts structured data from websites using **Crawl4AI** and **OpenAI LLMs**, and exposes the extracted data through a **FastAPI REST API**.

The scraper crawls a webpage, sends cleaned content to an LLM, extracts structured book data, and stores it as JSON.
The API layer then allows users to query the dataset, perform semantic search, or ask AI questions using a **RAG (Retrieval-Augmented Generation) pipeline**.

This project demonstrates how to combine **modern AI tools, web scraping, backend APIs, semantic search, and CI/CD pipelines** to build an intelligent data pipeline.

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
* ❤️ **Health check endpoint** for monitoring
* 🛡️ **Docker healthcheck support**
* 🔄 **CI/CD pipeline** using GitHub Actions
* 📦 **Automatic Docker image build & push to DockerHub**

---

## 🧠 Architecture

```id="y9b2kq"
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
   ↓
Docker Container
   ↓
CI/CD (GitHub Actions → DockerHub)
```

---

## 📂 Project Structure

```id="2w2m6v"
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
├── rag/
│   ├── vector_store.py
│   └── rag_pipeline.py
│
└── .github/
    └── workflows/
        └── docker.yml
```

---

## ⚙️ Installation (Local Setup)

```bash id="3ujg1n"
git clone <repo-url>
cd crawl4ai-book-scraper

python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash id="u5ahb2"
pip install -r requirements.txt
playwright install chromium
```

---

## 🔑 Environment Variables

Create a `.env` file:

```id="l2u6kz"
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Scraper

```bash id="m1p6h0"
python main.py
```

Generates:

```id="d7ml3n"
data/books.json
```

---

## ▶️ Run the API (Local)

```bash id="dgrz5m"
uvicorn api:app --reload
```

* API: http://127.0.0.1:8000
* Docs: http://127.0.0.1:8000/docs

---

## 🐳 Run with Docker

```bash id="kq1d7f"
docker compose up --build
```

* API: http://localhost:8000
* Docs: http://localhost:8000/docs

---

## ❤️ Health Check

```id="p7w8hf"
GET /health
```

Response:

```json id="2nqlhx"
{
  "status": "healthy",
  "service": "book-ai-api"
}
```

---

## 📡 API Endpoints

### Get all books

```id="3cbizb"
GET /books
```

### Get book by title

```id="i0q3v7"
GET /books?title=Sapiens
```

### Ask AI (Full Dataset)

```id="s7u6r8"
GET /ask?question=Which books cost more than £50?
```

### Ask AI (RAG)

```id="b6r5o2"
GET /ask-rag?question=Which books cost less than £50?
```

---

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** to automate Docker builds and deployment.

### Workflow:

```id="m2n4y9"
Push to main branch
        ↓
GitHub Actions triggered
        ↓
Docker image build
        ↓
Push to DockerHub (dhiraj918106/book-ai-api)
```

### Workflow File

```id="x9t6pq"
.github/workflows/docker.yml
```

### Required GitHub Secrets

```id="z8k1vn"
DOCKERHUB_USERNAME=dhiraj918106
DOCKERHUB_TOKEN=your_dockerhub_access_token
```

---

## 📦 Docker Image

Available at:

```id="v4y8os"
https://hub.docker.com/r/dhiraj918106/book-ai-api
```

---

## 🎯 Use Cases

* AI-powered web scraping
* Automated dataset generation
* Backend AI services
* Semantic search systems
* RAG-based applications

---

## 📌 Notes

* Uses practice website: https://books.toscrape.com
* Designed for learning **AI + RAG + DevOps pipelines**

---

## 📜 License

MIT License
