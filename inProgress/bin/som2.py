from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import lxml

headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 OPR/72.0.3815.378"}
r = requests.get("https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5T6CZ6/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.0wUJxkajdW_AXocIRrc54ysXU75fq8Y4zSe_afkYWsLDtC-yfdnogJsxNFHjtyZRizyAoygfaQDRD15ZqimDaEo67YZ0msPlW77FWQVjmG0zQG2APt3nLqU7X05tVexXHfeYTirgNg999Ec7A6old5ZfDqv1ZNcWx2VTozoifLTSMuz8SqKc8gHbGfckDLTubm7FJMsYcrkT5JeyWqQegpPZDYopxXySmT0zetW8zUs.SvYOrXL1QDdhSR0K9zaTBrO0QWJNcwipJaTeipAlSYw&dib_tag=se&keywords=macbook&qid=1713349039&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",headers=headers_param)
soup = BeautifulSoup(r.content,"lxml")

import re

price = soup.find("span", attrs={"class": "aok-offscreen"})
print(price)
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

