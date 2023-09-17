import requests;
import re;

from pages.books_page import BooksPage;

page_array = [];

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
            
#def print_output():
    # page_content = requests.get("https://books.toscrape.com/").content;
    # page = BooksPage(page_content)

    # for book in page.books:
    #     print(book)

#print_output();