import requests
from bs4 import BeautifulSoup
import pandas as pd

# Storage lists
Names = []
Prices = []
Descriptions = []
Reviews = []

# Base URL and pagination loop
base_url = "http://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page="

# Loop through pages (you can set max to what exists)
for page in range(1, 5):  # Try page=1 to 4, adjust as needed
    print(f"Scraping Page {page}...")
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find product boxes
    big_box = soup.find_all("div", {'class': 'col-md-4 col-xl-4 col-lg-4'})

    for box in big_box:
        try:
            name = box.find("a", {"class": "title"})['title'].strip()
            price = box.find("h4", {"class": "price float-end card-title pull-right"}).text.strip()
            desc = box.find("p", {"class": "description card-text"}).text.strip()
            reviews = box.find("p", {"class": "review-count float-end"}).text.strip()

            Names.append(name)
            Prices.append(price)
            Descriptions.append(desc)
            Reviews.append(reviews)

        except Exception as e:
            print(f"Error on page {page}:", e)
            continue

# Make DataFrame
df = pd.DataFrame({
    "Name": Names,
    "Price": Prices,
    "Description": Descriptions,
    "Reviews": Reviews
})

# Show data
print(df)
# Optional: df.to_csv("all_laptops.csv", index=False)
