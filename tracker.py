import pandas as pd
from scraper import get_product_data

URL = "PRODUCT_URL"

product = get_product_data(URL)

df = pd.DataFrame([product])

df.to_csv("data/prices.csv", mode="a", header=False, index=False)

print("Data saved successfully")
