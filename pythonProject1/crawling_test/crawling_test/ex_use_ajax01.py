from bs4 import BeautifulSoup
from day5.mydb import Mydb
import requests
import json

db = Mydb()


headers = {"referer": 'https://finance.daum.net',
            "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def fn_kospi():
    # url = 'http://finance.daum.net/domestic/kospi'
    url = 'http://finance.daum.net/api/search/ranks?limit=10'
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())


fn_kospi()