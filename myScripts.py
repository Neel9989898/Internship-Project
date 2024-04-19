# from tinydb import TinyDB, Query
# import hashlib
# from bs4 import BeautifulSoup
# import requests
# import threading
# from flask import Flask, request, render_template, jsonify
# import time
# from datetime import datetime
# import email
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import uuid 
# import scrapy
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings

# # Configure your Email
# email_address = "example@example.com"
# email_password = "ExamplePassword"
# email_smtp_server = "smtp.example.com"
# email_smtp_port = 587
# # Configure End

# def send_email(address,content):
#     # Your existing email sending code here

# def get_product(url):
#     headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.378"}
#     r = requests.get(url, headers=headers_param)
#     soup = BeautifulSoup(r.content,"lxml")
    
#     # Extracting price
#     price = soup.find("span", attrs={"class": "aok-offscreen"})
#     if price:
#         # Get the text content of the price element
#         price_text = price.text.strip()
        
#         # Use regular expressions to extract price with currency
#         match = re.search(r'(\D*)([\d,.]+)\s*(\w+)', price_text)
#         if match:
#             price_with_currency = match.group(1) + match.group(2) + ' ' + match.group(3)
#         else:
#             price_with_currency = "Price format not recognized"
#     else:
#         price_with_currency = "Price not found"
    
#     # Extracting description
#     description = soup.find("span", attrs={"id": "productTitle"})
#     if description:
#         description = description.text.strip()
#     else:
#         description = "Description not found"
    
#     # Extracting customer ratings
#     ratings = soup.find("span", attrs={"id": "acrCustomerReviewText"})
#     if ratings:
#         ratings = ratings.text.strip()
#     else:
#         ratings = "Customer Ratings not found"
    
#     # Extracting the number of customer reviews
#     reviews = soup.find("span", attrs={"id": "acrPopover"})
#     if reviews:
#         reviews = reviews.text.strip()
#     else:
#         reviews = "Number of Reviews not found"
    
#     # Extracting images
#     images = soup.find_all("img", attrs={"class": "a-dynamic-image"})
#     image_urls = []
#     if images:
#         for image in images:
#             src = image["src"]
#             image_urls.append(src)
#     else:
#         image_urls = ["Product images not found"]
    
#     # Extracting specifications
#     specifications = soup.find("div", attrs={"id": "productOverview_feature_div"})
#     specs_dict = {}
#     if specifications:
#         rows = specifications.find_all("tr")
#         for row in rows:
#             cells = row.find_all("td")
#             if cells:
#                 key = cells[0].text.strip()
#                 value = cells[1].text.strip()
#                 specs_dict[key] = value
#     else:
#         specs_dict = {"Product specifications not found"}
    
#     return {
#         "url": url,
#         "price": price_with_currency,
#         "description": description,
#         "ratings": ratings,
#         "reviews": reviews,
#         "image_urls": image_urls,
#         "specifications": specs_dict
#     }

# def check_amazon():
#     # Your existing check_amazon function here

# # # Scrapy spider definition
# # class AmazonSpider(scrapy.Spider):
# #     name = "amazon"
# #     start_urls = [
# #         'https://www.amazon.in/Logitech-G512-Mechanical-Keyboard-Black/dp/B07BVCSRXL',
# #         # Add more product URLs here if needed
# #     ]

# #     def parse(self, response):
# #         # Your Scrapy spider logic here
# #         pass

# # Function to trigger Scrapy spider
# def scrape_amazon():
#     process = CrawlerProcess(get_project_settings())
#     process.crawl(AmazonSpider)
#     process.start() # the script will block here until the crawling is finished

# app = Flask("Python Amazon Price Tracker") 

# # Routes

# # Route to trigger Scrapy spider
# @app.route('/scrape_amazon', methods=['GET'])
# def trigger_scrapy():
#     threading.Thread(target=scrape_amazon).start()
#     return 'Scraping initiated!'

# # Your existing routes here

# if __name__ == '__main__':
#     threading.Thread(target=check_amazon).start()
#     app.run(host='0.0.0.0', debug=False, port=10086)
