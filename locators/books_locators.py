class BookLocators:
    TITLE = 'h3 a' #you will need to do something like if title_element: title = title_element['title'] print("Title:", title)
    RATING = ('p.star-rating')  # print(title['class'][-1]);
    PRICE = 'div.product_price p.price_color' #print(title.text);
    IN_STOCK = 'p.availability'; #title.text.strip()