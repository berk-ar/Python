import requests
from bs4 import BeautifulSoup

def basic_scraping_example():
    url = "http://books.toscrape.com/"  # test site

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Kitap başlıklarını bul
        books = soup.select("h3 a") # CSS selector

        # print(books)

        print("Kitap listesi: ")
        for i, book in enumerate(books[:10], 1): # ilk 10 kitap
            print(f"{i:2d}. {book.text.strip()}")

    except Exception as e:
        print("Hata:",e)
    
# Çalıştır
basic_scraping_example()