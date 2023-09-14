class BookLocators:
    TITLE = 'h3 a' #you will need to do something like if title_element: title = title_element['title'] print("Title:", title)
    RATING = ('p.star-rating') #print(title['class'][-1]);
    PRICE = 'div.productprice p.price_color' #print(title.text);
    IN_STOCK = 'p.availability i.icon-ok'; #title.text.strip()


# import requests
# from bs4 import BeautifulSoup

# # URL of the website
# url = 'https://books.toscrape.com/'

# # Send a GET request to the URL and fetch the HTML content
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')
#     # Use the locator to find the first title element
#     title_element = soup.select_one(f'article.product_pod p.availability')
    
#     # Extract the title text
#     if title_element:
#         title = title_element
#         print(title.text.strip());
#     else:
#         print("Title element not found")
# else:
#     print("Failed to retrieve the webpage. Status code:", response.status_code)