# 📚 AI Web Scraper — Crawl4AI + OpenAI

A simple AI-powered web scraping project that extracts structured data from websites using **Crawl4AI** and **OpenAI LLMs**.

The scraper crawls a webpage, sends the cleaned content to an LLM, and returns structured JSON data.

This project demonstrates how to combine modern AI tools with web scraping to build intelligent data extraction pipelines.

---

## 🚀 Features

* 🕸️ **Async Web Crawling** using Crawl4AI
* 🌐 **Browser Rendering** powered by Playwright
* 🤖 **AI Data Extraction** using OpenAI models
* 📦 **Structured Data Validation** with Pydantic
* 🔐 **Secure API Key Management** using python-dotenv
* 📄 Saves extracted data as **clean JSON**

---

## 🧠 How It Works

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
```

---

## 📂 Project Structure

```
crawl4ai-book-scraper
│
├── .env
├── main.py
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
pip install crawl4ai openai python-dotenv pydantic
playwright install chromium
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Project

```bash
python main.py
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
* Data extraction pipelines
* LLM-assisted web crawling
* Building datasets for AI/RAG systems

---

## 📌 Notes

* Designed for **learning AI-based scraping**
* Uses a practice website:

https://books.toscrape.com

* Avoid scraping websites that prohibit automated access.

---

## 📜 License

MIT License
