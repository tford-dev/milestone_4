import requests;

from pages.books_page import BooksPage;

page_content = requests.get("https://books.toscrape.com/").content
page = BooksPage(page_content)
page_array = [];
for book in page.books:
    page_array.append({
        'Title': book.title,
        'Rating': book.rating,
        'Price': book.price,
        'Availability': book.in_stock
    })

#def print_output():
    # page_content = requests.get("https://books.toscrape.com/").content;
    # page = BooksPage(page_content)

    # for book in page.books:
    #     print(book)

#print_output();