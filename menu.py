from app import *;
import logging;

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s:%(message)s', 
    level=logging.DEBUG,
    filename='logs.txt'
);

USER_CHOICE = """
Enter:
- 'a' to print all books
- 'b' to print the best books
- 'p' to print books based on a desired price
- 'q' or any other key to quit entire process
Your choice: """
def print_all_books():
    if len(page_array) > 0:
        for book in page_array:
            print(book);
        logging.info("Data in print_all_books() have been printed.")
    else: 
        print("There is no data for your query, adjust page number.")
        logging.debug("page_array is empty, no data to output to user. Bad query.")


def print_best_books():
    while True: 
        rating_input = input("What is your desired rating for a book? ")
        if rating_input == 'q':
            logging.info("User quit session in print_best_books().")
            break;
        try:
            rating = float(rating_input)
            print_best_books_array = [];
            logging.info(f"Added data to print_best_books_array[]. {print_best_books_array}")
            for book in page_array:
                if rating == book['Rating']:
                    print_best_books_array.append(book);
            if len(print_best_books_array) > 0:
                for book in print_best_books_array:
                    print(f"{book['Title']} has a rating of {book['Rating']} out of 5 stars.");
                logging.info(f"Results from request for best books have been printed. {print_best_books_array}")
            else:
                print(f"As it stands, there are no books of the rating: {rating_input}");
                logging.debug("Result for calling print_best_books() was null.")
            break;
        except ValueError:
            print("Invalid input, please enter a valid number for book rating!!! >:O")
            logging.warning("Invalid input by user for print_best_books().")
            
def print_price():
    while True:
        price = input("What is your desired price for a book??? ")
        if price == 'q':
            logging.info("User quit session in print_price().")
            break
        try:
            print_price_array = [];
            for book in page_array:
                float_price = float(book['Price']);
                if (float_price <= float(price)):
                    print_price_array.append(book);
            logging.info(f"Added data to print_price_array[]. {print_price_array}")
            print_price_array_sorted = sorted(print_price_array, key=lambda x: x['Price'] * -1)[:10];
            logging.info(f"Sorted data in print_price_array[]")
            if len(print_price_array) > 0:
                for book in print_price_array_sorted:
                    print(f"{book['Title']} is close to your desired price of £{float(price)}, this book costs £{book['Price']}.");
                logging.info(f"Results for request for print_price() have been printed {print_price_array_sorted}")
            else: 
                print("Please get your bread up.");
                logging.debug("Result for calling print_price() was null.")
            break;
        except ValueError:
            print("Invalid input, please enter a valid number for book price!!! >:O");
            logging.warning("Invalid input by user for print_price().")

def menu():
    while True:
        page_prompt();
        user_input = input(USER_CHOICE);
        if user_input.lower() == 'a':
            logging.info("User entered 'a' and called print_all_books().")
            print_all_books();
        elif user_input.lower() == 'b':
            logging.info("User entered 'b' and called print_best_price().")
            print_best_books();
        elif user_input.lower() == 'p':
            logging.info("User entered 'p' and called print_price().")
            print_price();
        elif user_input.lower() == 'q':
            logging.info("User quit session.")
            print("Process terminated.");
            break;
        else:
            logging.warning("Invalid input from user in menu() function.")
            print("Invalid choice. \nPlease choose a valid option");
            
menu();