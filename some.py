import requests
from bs4 import BeautifulSoup
def get_amazon_price(url):
    # Set headers to mimic a browser visit
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.prettify())
        # Find the element containing the price
        price_element = soup.find(id='twisterPlusWWDesktop')  # You may need to adjust the ID based on the structure of the Amazon page
        
        if price_element:
            # Extract the price text
            price_text = price_element.get_text()
            # Clean the price text (remove extra characters, whitespace, etc.)
            price_text = price_text.strip()
            return price_text
        else:
            return "Price not found."
    else:
        return "Failed to fetch page."

# Example usage
if __name__ == "__main__":
    amazon_url = 'https://www.amazon.in/Logitech-G512-Mechanical-Keyboard-Black/dp/B07BVCSRXL'
    price = get_amazon_price(amazon_url)
    print("Price:", price)
