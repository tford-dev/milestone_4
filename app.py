import requests
import re
import aiohttp
import async_timeout
import asyncio
import time

from pages.books_page import BooksPage;

page_array = [];

async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f"Page took {time.time() - page_start} to finish.")
            return response.status
        
async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

def page_prompt():
    while True:
        try:
            page_input_prompt = input("Whoa there, what page would you like to search from?\nPress enter to continue on page 1.\nPress 'c' to continue(you must continue if you'd like to terminate this process).\n");
            if page_input_prompt == 'c':
                break
            page_content = '';
            if page_input_prompt == '':
                page_content = requests.get(
                    f"https://books.toscrape.com/catalogue/page-1.html").content
            elif int(page_input_prompt):
                page_content = requests.get(
                    f"https://books.toscrape.com/catalogue/page-{page_input_prompt}.html").content
            page = BooksPage(page_content)
            page_array.clear();
            for book in page.books:
                formatted_price = re.sub(r'£', '', book.price);
                float_price = float(formatted_price);
                page_array.append({
                    'Title': book.title,
                    'Rating': book.rating,
                    'Price': float_price,
                    'Availability': book.in_stock
                })
            break;
        except ValueError:
            print("Please enter a number for desired page or press enter in order for input to be valid.")