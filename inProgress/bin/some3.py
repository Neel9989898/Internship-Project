import requests
from bs4 import BeautifulSoup
import re

# Send an HTTP request to the webpage you want to scrape
response = requests.get("https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5T6CZ6/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.0wUJxkajdW_AXocIRrc54ysXU75fq8Y4zSe_afkYWsLDtC-yfdnogJsxNFHjtyZRizyAoygfaQDRD15ZqimDaEo67YZ0msPlW77FWQVjmG0zQG2APt3nLqU7X05tVexXHfeYTirgNg999Ec7A6old5ZfDqv1ZNcWx2VTozoifLTSMuz8SqKc8gHbGfckDLTubm7FJMsYcrkT5JeyWqQegpPZDYopxXySmT0zetW8zUs.SvYOrXL1QDdhSR0K9zaTBrO0QWJNcwipJaTeipAlSYw&dib_tag=se&keywords=macbook&qid=1713349039&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "lxml")

# Extract the title of the product
title = soup.find("span", attrs={"id": "productTitle"})
if title:
    title = title.text.strip()
    print("Title:", title)
else:
    print("Title not found")

# Extract the price of the product
price = soup.find("span", attrs={"class": "aok-offscreen"})
if price:
    price_text = price.text.strip()
    match = re.search(r'([\D\s]*)([\d,.]+)\s*(\w+)', price_text)
    if match:
        price_with_currency = match.group(2) + ' ' + match.group(3)
        print("Price with currency:", price_with_currency)
    else:
        print("Price format not recognized")
else:
    print("Price not found")

# Extract the product description
description = soup.find("div", attrs={"id": "productDescription"})
if description:
    description = description.text.strip()
    print("Description:", description)
else:
    print("Description not found")

# Extract the product features
features = soup.find_all("tr", attrs={"class": "a-keyvalue"})
for feature in features:
    key = feature.find("th", attrs={"class": "a-size-base a-spacing-mini a-color-base s-product-attribute-label"})
    if key:
        key = key.text.strip()
    value = feature.find("td", attrs={"class": "a-size-base a-spacing-mini a-color-base s-product-attribute-value"})
    if value:
        value = value.text.strip()
    if key and value:
        print(key, ":", value)

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