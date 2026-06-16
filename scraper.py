import requests
from bs4 import BeautifulSoup

print("=====================================")
print("     LIVE BOOKSTORE SCRAPER: ALL     ")
print("=====================================")

URL = "http://books.toscrape.com/"

def scrape_all_books():
    response = requests.get(URL)
    response.encoding = 'utf-8'
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # FIX: Changing .find() to .find_all() collects EVERY book card into a list
    all_books = soup.find_all("article", class_="product_pod")

    print(f"Found {len(all_books)} books on the homepage!\n")
    print("--------------------------------------------------")

    # Loop through our list of 20 books one by one
    for index, book in enumerate(all_books, start=1):
        # Extract individual titles and prices safely inside the loop
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        
        # Clean up the output text by pulling out extra characters if needed
        print(f"{index}. 📖 {title}")
        print(f"   💰 Price: {price}")
        print("--------------------------------------------------")

if __name__ == "__main__":
    scrape_all_books()