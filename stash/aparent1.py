import scrapy
from bs4 import BeautifulSoup
import re
import smtplib

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        'https://www.amazon.in/Logitech-G512-Mechanical-Keyboard-Black/dp/B07BVCSRXL',
    ]
    
    # Set your target price
    target_price = 2000

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        # Extracting price
        price = soup.find("span", attrs={"class": "aok-offscreen"})
        if price:
            price_text = price.text.strip()
            match = re.search(r'(\D*)([\d,.]+)\s*(\w+)', price_text)
            if match:
                price_with_currency = float(match.group(2).replace(',', ''))
                price_with_currency_str = match.group(1) + match.group(2) + ' ' + match.group(3)
            else:
                price_with_currency = None
                price_with_currency_str = "Price format not recognized"
        else:
            price_with_currency = None
            price_with_currency_str = "Price not found"

        # Price tracking logic
        if price_with_currency and price_with_currency < self.target_price:
            self.send_notification(price_with_currency_str)

        # Extracting other information
        description = soup.find("span", attrs={"id": "productTitle"})
        if description:
            description = description.text.strip()
        else:
            description = "Description not found"

        ratings = soup.find("span", attrs={"id": "acrCustomerReviewText"})
        if ratings:
            ratings = ratings.text.strip()
        else:
            ratings = "Customer Ratings not found"

        reviews = soup.find("span", attrs={"id": "acrPopover"})
        if reviews:
            reviews = reviews.text.strip()
        else:
            reviews = "Number of Reviews not found"

        images = soup.find_all("img", attrs={"class": "a-dynamic-image"})
        image_urls = []
        if images:
            for image in images:
                src = image["src"]
                image_urls.append(src)
        else:
            image_urls = ["Product images not found"]

        specifications = soup.find("div", attrs={"id": "productOverview_feature_div"})
        if specifications:
            rows = specifications.find_all("tr")
            specs = {}
            for row in rows:
                cells = row.find_all("td")
                if cells:
                    key = cells[0].text.strip()
                    value = cells[1].text.strip()
                    specs[key] = value
        else:
            specs = {"Product specifications": "not found"}

        yield {
            "Description": description,
            "Price": price_with_currency_str,
            "Customer Ratings": ratings,
            "Number of Reviews": reviews,
            "Image URLs": image_urls,
            "Specifications": specs,
        }

    def send_notification(self, price):
        # Send notification via email
        sender_email = "neel.patel@rapidops.co"
        receiver_email = "dhrumil.patel@rapidops.com"
        password = "Mar#2003!@"

        message = f"Price dropped below target price! Current price: {price}"

        with smtplib.SMTP_SSL("smtp.rapidops.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

