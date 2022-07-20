import requests
from bs4 import BeautifulSoup

url = 'https://www.msn.com/ko-kr/news'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.text)