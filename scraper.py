import requests
from bs4 import BeautifulSoup

print("=====================================")
print("        LIVE BOOK WEB SCRAPER        ")
print("=====================================")

URL = "http://books.toscrape.com/"

def scrape_book_info():
    # 1. Send an HTTP request to the website
    response = requests.get(URL)
    
    # FIX: Explicitly set the encoding to UTF-8 to handle currency symbols cleanly
    response.encoding = 'utf-8'
    
    # Check if the website connected successfully
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    # 2. Feed the raw HTML text into BeautifulSoup to organize it
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Target the container holding the first book item
    first_book = soup.find("article", class_="product_pod")

    if first_book:
        title = first_book.h3.a["title"]
        price = first_book.find("p", class_="price_color").text
        
        # Print out our clean, extracted results!
        print("\nSuccessfully extracted live data:")
        print(f"📖 Book Title: {title}")
        print(f"💰 Book Price: {price}")
    else:
        print("Could not find any book elements on the page.")

if __name__ == "__main__":
    scrape_book_info()