from bs4 import BeautifulSoup
import requests
import re

def scrape_amazon_product(url):
    # Define user agent headers
    headers_param = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.378"
    }
    
    # Send request to the URL
    r = requests.get(url, headers=headers_param)
    soup = BeautifulSoup(r.content, "lxml")

    # Extract the price
    price = soup.find("span", attrs={"class": "aok-offscreen"})
    if price:
        price_text = price.text.strip()
        match = re.search(r"(\D*)([\d,.]+)\s*(\w+)", price_text)
        if match:
            price_with_currency = match.group(1) + match.group(2) + " " + match.group(3)
            price_value = float(match.group(2).replace(",", ""))
        else:
            price_with_currency = "Price format not recognized"
            price_value = None
    else:
        price_with_currency = "Price not found"
        price_value = None

    # Extract the product description
    description = soup.find("span", attrs={"id": "productTitle"})
    description = description.text.strip() if description else "Description not found"

    # Extract the customer ratings
    ratings = soup.find("span", attrs={"id": "acrCustomerReviewText"})
    ratings = ratings.text.strip() if ratings else "Customer Ratings not found"

    # Extract the number of customer reviews
    reviews = soup.find("span", attrs={"id": "acrPopover"})
    reviews = reviews.text.strip() if reviews else "Number of Reviews not found"

    return {
        # "url": url,
        "description": description,
        "price_with_currency": price_with_currency[0:-4],
        "price_value": price_value,
        "ratings": ratings,
        "reviews": reviews,
    }

# Example usage:
url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5T6CZ6/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.0wUJxkajdW_AXocIRrc54ysXU75fq8Y4zSe_afkYWsLDtC-yfdnogJsxNFHjtyZRizyAoygfaQDRD15ZqimDaEo67YZ0msPlW77FWQVjmG0zQG2APt3nLqU7X05tVexXHfeYTirgNg999Ec7A6old5ZfDqv1ZNcWx2VTozoifLTSMuz8SqKc8gHbGfckDLTubm7FJMsYcrkT5JeyWqQegpPZDYopxXySmT0zetW8zUs.SvYOrXL1QDdhSR0K9zaTBrO0QWJNcwipJaTeipAlSYw&dib_tag=se&keywords=macbook&qid=1713349039&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
result = scrape_amazon_product(url)
print(result)
