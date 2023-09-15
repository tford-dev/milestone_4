from locators.books_locators import BookLocators;

class BookParser:
    def __init__(self, parent):
        self.parent = parent;

    def __repr__(self):
        return f"The book '{self.title}' has {self.rating} stars. The book is {self.price} and is {self.in_stock}.";

    @property
    def title(self):
        locator = BookLocators.TITLE;
        return self.parent.select_one(locator)['title']
    
    @property
    def rating(self):
        locator = BookLocators.RATING;
        return self.parent.select_one(locator)['class'][-1].lower()
    
    @property
    def price(self):
        locator = BookLocators.PRICE;
        return self.parent.select_one(locator).text
    
    @property
    def in_stock(self):
        locator = BookLocators.IN_STOCK;
        return self.parent.select_one(locator).text.strip().lower()