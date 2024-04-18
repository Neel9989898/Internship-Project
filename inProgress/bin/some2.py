import requests
from lxml import html

def get_amazon_product_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = html.fromstring(response.content)

    try:
        title = soup.xpath('//span[@id="productTitle"]/text()')[0].strip()
    except:
        title = None

    try:
        price = soup.xpath('//span[@class="a-offscreen"]/text()')[0].strip().replace(',', '').replace('₹', '').replace('.00', '')
    except:
        price = None

    try:
        rating = soup.xpath('//i[@class="a-icon-star"]/text()')[0].strip()
    except:
        rating = None

    try:
        specs_obj = {}
        specs = soup.xpath('//tr[@class="a-spacing-small"]')
        for spec in specs:
            key = spec.xpath('./td[1]/text()')[0].strip()
            value = spec.xpath('./td[2]/text()')[0].strip()
            specs_obj[key] = value
        specs_arr = [specs_obj]
    except:
        specs_arr = None

    return {
        'title': title,
        'price': price,
        'rating': rating,
        'specs': specs_arr
    }


bucket_list = ['https://www.amazon.in/BenQ-inch-Bezel-Monitor-Built/dp/B073NTCT4R/']

for url in bucket_list:
    print(get_amazon_product_details(url))