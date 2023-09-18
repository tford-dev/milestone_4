from app import *;

USER_CHOICE = """
Enter:
- 'a' to print all books
- 'b' to print the best books
- 'p' to print books based on a desired price
- 'q' or any other key to quit entire process
Your choice: """
def print_all_books():
    for book in page_array:
        print(book);


def print_best_books():
    while True: 
        rating_input = input("What is your desired rating for a book? ")
        if rating_input == 'q':
            break;
        try:
            rating = float(rating_input)
            print_best_books_array = [];
            for book in page_array:
                if rating == book['Rating']:
                    print_best_books_array.append(book);
            if len(print_best_books_array) > 0:
                for book in print_best_books_array:
                    print(f"{book['Title']} has a rating of {book['Rating']} out of 5 stars.");
            else:
                print(f"As it stands, there are no books of the rating: {rating_input}");
            break;
        except ValueError:
            print("Invalid input, please enter a valid number for book rating!!! >:O")
            
def print_price():
    while True:
        price = input("What is your desired price for a book??? ")
        if price == 'q':
            break
        try:
            print_price_array = [];
            for book in page_array:
                float_price = float(book['Price']);
                if (float_price <= float(price)):
                    print_price_array.append(book);
            print_price_array_sorted = sorted(print_price_array, key=lambda x: x['Price'] * -1)[:10];
            if len(print_price_array) > 0:
                for book in print_price_array_sorted:
                    print(f"{book['Title']} is close to your desired price of £{float(price)}, this book costs £{book['Price']}.");
            else: 
                print("Please get your bread up.");
            break;
        except ValueError:
            print("Invalid input, please enter a valid number for book price!!! >:O");
    
def menu():
    while True:
        page_prompt();
        user_input = input(USER_CHOICE);
        if user_input.lower() == 'a':
            print_all_books();
        elif user_input.lower() == 'b':
            print_best_books();
        elif user_input.lower() == 'p':
            print_price();
        elif user_input.lower() == 'q':
            print("Process terminated.");
            break;
        else:
            print("Invalid choice. \nPlease choose a valid option");
            
menu();