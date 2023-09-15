from locators.books_locators import BookLocators;

class BookParser:
    
    def __init__(self, parent):
        self.parent = parent;

    def __repr__(self):
        return {
            'Title' : {self.title}, 
            'Rating' : {self.rating}, 
            'Price' : {self.price}, 
            'Availability' : {self.in_stock}
        };

    @property
    def title(self):
        locator = BookLocators.TITLE;
        return self.parent.select_one(locator)['title']
    
    @property
    def rating(self):
        RATINGS = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        locator = BookLocators.RATING;
        rating_string = self.parent.select_one(locator)['class'][-1]
        if rating_string in RATINGS:
            number = RATINGS[rating_string];
            return number
        else:
            return None;
        
    
    @property
    def price(self):
        locator = BookLocators.PRICE;
        return self.parent.select_one(locator).text
    
    @property
    def in_stock(self):
        locator = BookLocators.IN_STOCK;
        return self.parent.select_one(locator).text.strip().lower()