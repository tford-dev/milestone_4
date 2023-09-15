from app import page_array;

def print_best_books(rating):
    for book in page_array:
        if rating == book['Rating']:
            print(f"{book['Title']} has a rating of {book['Rating']} out of 5 stars.");
    
print_best_books(5);