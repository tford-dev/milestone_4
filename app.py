import requests;
import re;

from pages.books_page import BooksPage;

page_content = requests.get("https://books.toscrape.com/").content
page = BooksPage(page_content)
page_array = [];
for book in page.books:
    formatted_price = re.sub(r'£', '', book.price);
    float_price = float(formatted_price);
    page_array.append({
        'Title': book.title,
        'Rating': book.rating,
        'Price': float_price,
        'Availability': book.in_stock
    })

#def print_output():
    # page_content = requests.get("https://books.toscrape.com/").content;
    # page = BooksPage(page_content)

    # for book in page.books:
    #     print(book)

#print_output();