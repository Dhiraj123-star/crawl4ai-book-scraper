import os
import json
from dotenv import load_dotenv
from crawl4ai import AsyncWebCrawler
from openai import OpenAI

from scraper.schema import BookList

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def scrape_books():

    url = "https://books.toscrape.com/"

    # Step 1: Crawl page
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)

    markdown_content = result.markdown[:12000]

    # Step 2: Send to OpenAI
    prompt = f"""
You are a strict data extraction engine.

Extract book title and price from the page.

Return ONLY valid JSON with this structure:

{{
"books": [
{{"title": "...", "price": "..."}}
]
}}

Do not return markdown.
Do not return explanations.
Do not wrap the JSON.

Page content:
{markdown_content}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You extract structured data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    raw_output = response.choices[0].message.content.strip()

    # Remove accidental markdown fences if LLM adds them
    raw_output = raw_output.replace("```json", "").replace("```", "")

    parsed = json.loads(raw_output)

    return BookList(**parsed)