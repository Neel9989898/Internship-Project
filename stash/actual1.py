from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as npk
import lxml
url="https://www.amazon.in/Logitech-G512-Mechanical-Keyboard-Black/dp/B07BVCSRXL"
headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.378"}
r = requests.get(url,headers=headers_param)
soup = BeautifulSoup(r.content,"lxml")
# print(soup.prettify())

import re

price = soup.find("span", attrs={"class": "aok-offscreen"})
if price:
    # Get the text content of the price element
    price_text = price.text.strip()
    
    # Use regular expressions to extract price with currency
    match = re.search(r'(\D*)([\d,.]+)\s*(\w+)', price_text)
    if match:
        price_with_currency = match.group(1) + match.group(2) + ' ' + match.group(3)
        # print("Price with currency:", price_with_currency[0:-4])
    else:
        print("Price format not recognized")
else:
    print("Price not found")



# Extract the product description
description = soup.find("span", attrs={"id": "productTitle"})
if description:
    description = description.text.strip()
    print(f"Description : {description} \nPrice : {price_with_currency[0:-4]}")
else:
    print("Description not found")

# Extract the customer ratings
ratings = soup.find("span", attrs={"id": "acrCustomerReviewText"})
if ratings:
    ratings = ratings.text.strip()
    print("Customer Ratings:", ratings)
else:
    print("Customer Ratings not found")

# Extract the number of customer reviews
reviews = soup.find("span", attrs={"id": "acrPopover"})
if reviews:
    reviews = reviews.text.strip()
    print("Number of Reviews:", reviews)
else:
    print("Number of Reviews not found")



images = soup.find_all("img", attrs={"class": "a-dynamic-image"})
if images:
    for image in images:
        src = image["src"]
        print("Image URL:", src)
else:
    print("Product images not found")


specifications = soup.find("div", attrs={"id": "productOverview_feature_div"})
if specifications:
    rows = specifications.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if cells:
            key = cells[0].text.strip()
            value = cells[1].text.strip()
            print(key, ":", value)
else:
    print("Product specifications not found")