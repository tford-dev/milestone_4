def print_output():
    page_content = requests.get("https://books.toscrape.com/").content;
    page = BooksPage(page_content)

    for book in page.books:
        print(book)

print_output();