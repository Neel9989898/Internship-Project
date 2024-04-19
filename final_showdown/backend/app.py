from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import logging
import re
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
logger = logging.getLogger(__name__)

@app.route('/scrape', methods=['GET'])
def scrape_product():
    url = request.args.get('url')
    # url = "https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5T6CZ6/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.0wUJxkajdW_AXocIRrc54ysXU75fq8Y4zSe_afkYWsLDtC-yfdnogJsxNFHjtyZRizyAoygfaQDRD15ZqimDaEo67YZ0msPlW77FWQVjmG0zQG2APt3nLqU7X05tVexXHfeYTirgNg999Ec7A6old5ZfDqv1ZNcWx2VTozoifLTSMuz8SqKc8gHbGfckDLTubm7FJMsYcrkT5JeyWqQegpPZDYopxXySmT0zetW8zUs.SvYOrXL1QDdhSR0K9zaTBrO0QWJNcwipJaTeipAlSYw&dib_tag=se&keywords=macbook&qid=1713349039&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400

    try:
        headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.378"}
        r = requests.get(url, headers=headers_param)
        soup = BeautifulSoup(r.content, "lxml")

        # Extracting price
        price = soup.find("span", attrs={"class": "aok-offscreen"})
        if price:
            price_text = price.text.strip()
            match = re.search(r'(\D*)([\d,.]+)\s*(\w+)', price_text)
            if match:
                price_with_currency = match.group(1) + match.group(2) + ' ' + match.group(3)
                print(price_with_currency[0:-4]);
            else:
                price_with_currency = "Price format not recognized"
                
                
        else:
            price_with_currency = "Price not found"
            print("error")

        # Extracting description
        description = soup.find("span", attrs={"id": "productTitle"})
        description = description.text.strip() if description else "Description not found"

        # Extracting customer ratings
        ratings = soup.find("span", attrs={"id": "acrCustomerReviewText"})
        ratings = ratings.text.strip() if ratings else "Customer Ratings not found"

        # Extracting number of customer reviews
        reviews = soup.find("span", attrs={"id": "acrPopover"})
        reviews = reviews.text.strip() if reviews else "Number of Reviews not found"

        # Extracting images
        images = soup.find_all("img", attrs={"class": "a-dynamic-image"})
        image_urls = [image["src"] for image in images] if images else ["Product images not found"]

        # Extracting specifications
        specifications = soup.find("div", attrs={"id": "productOverview_feature_div"})
        specifications = specifications.find_all("tr") if specifications else []

        specifications_dict = {}
        for row in specifications:
            cells = row.find_all("td")
            if cells:
                key = cells[0].text.strip()
                value = cells[1].text.strip()
                specifications_dict[key] = value

        return jsonify({
            "description": description,
            "price": price_with_currency[:-4],
            "customer_ratings": ratings,
            "number_of_reviews": reviews,
            "image_urls": image_urls,
            "specifications": specifications_dict
        })
        # return "testing"

    except Exception as e:
        logger.exception("An error occurred during scraping:")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
