import requests
from bs4 import BeautifulSoup

def get_product_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("span", id="productTitle").text.strip()
    price = soup.find("span", class_="a-price-whole").text.strip()

    return {
        "title": title,
        "price": price
    }
