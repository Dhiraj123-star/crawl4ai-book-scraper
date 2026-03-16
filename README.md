# 📚 AI Web Scraper & Book API — Crawl4AI + OpenAI + FastAPI

A simple **AI-powered web scraping and data service project** that extracts structured data from websites using **Crawl4AI** and **OpenAI LLMs**, and exposes the extracted data through a **FastAPI REST API**.

The scraper crawls a webpage, sends cleaned content to an LLM, extracts structured book data, and stores it as JSON.
The API layer then allows users to query the dataset or ask AI questions about it.

This project demonstrates how to combine **modern AI tools, web scraping, and backend APIs** to build an intelligent data pipeline.

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
* 🧠 **AI-powered Q&A endpoint** over the dataset

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
FastAPI Service
   ↓
REST API + AI Question Answering
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
│
├── data/
│   └── books.json
│
└── scraper/
    ├── crawler.py
    └── schema.py
```

---

## ⚙️ Installation

Clone the repository and create a virtual environment.

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

## ▶️ Run the API

Start the FastAPI server:

```bash
uvicorn api:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

Interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Get all books

```
GET /books
```

Returns the full dataset.

---

### Get book by title

```
GET /books?title=Sapiens
```

Returns the matching book.

---

### Ask AI about books

```
GET /ask?question=Which books cost more than £50?
```

The AI reads the dataset and answers the question.

Example response:

```json
{
  "question": "Which books cost more than £50?",
  "answer": "The following books cost more than £50: A Light in the Attic (£51.77), Sapiens: A Brief History of Humankind (£54.23)."
}
```

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
* Backend AI data services
* Building datasets for **RAG or AI search systems**

---

## 📌 Notes

* Designed for **learning AI-based scraping pipelines**
* Uses a practice website:

https://books.toscrape.com

* Avoid scraping websites that prohibit automated access.

---

## 📜 License

MIT License
