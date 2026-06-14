import requests
from bs4 import BeautifulSoup

print("=====================================")
print("        LIVE BOOK WEB SCRAPER        ")
print("=====================================")

URL = "http://books.toscrape.com/"

def scrape_book_info():
    # 1. Send an HTTP request to the website
    response = requests.get(URL)
    
    # Check if the website connected successfully (Status Code 200 means OK)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    # 2. Feed the raw HTML text into BeautifulSoup to organize it
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Target the container holding the first book item
    # On this website, each book is placed inside an HTML tag called an <article>
    first_book = soup.find("article", class_="product_pod")

    if first_book:
        # Extract the title from the <h3> link tag inside the article
        title = first_book.h3.a["title"]
        
        # Extract the price text from the HTML element with the class name 'price_color'
        price = first_book.find("p", class_="price_color").text
        
        # Print out our clean, extracted results!
        print("\nSuccessfully extracted live data:")
        print(f"📖 Book Title: {title}")
        print(f"💰 Book Price: {price}")
    else:
        print("Could not find any book elements on the page.")

if __name__ == "__main__":
    scrape_book_info()