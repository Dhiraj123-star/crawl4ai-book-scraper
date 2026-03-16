import asyncio
import json
from scraper.crawler import scrape_books

async def main():
    data = await scrape_books()

    with open("data/books.json","w") as f:
        json.dump(data.model_dump(),f,indent=2)
    
    print("Scraping completed!!")
    print(data.model_dump())

if __name__=="__main__":
    asyncio.run(main())