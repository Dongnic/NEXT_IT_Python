import requests
from bs4 import BeautifulSoup
import numpy as np
url = 'https://naver.me/GJrZWcMF'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())