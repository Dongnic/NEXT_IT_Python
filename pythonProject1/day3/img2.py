# 영화페이지의 이미지를 movie_poster 폴더에 저장하시오
import urllib.request as req
import os

import requests
from bs4 import BeautifulSoup as bs

path = os.getcwd()
moviedir = path + '/img/movie_poster/'
if os.path.isdir(moviedir):
    print('폴더 있음')
else:
    #폴더 생성
    os.mkdir(moviedir)
url = 'https://movie.naver.com/movie/running/current.naver'
res = requests.get(url)
soup = bs(res.text, 'html.parser')
ul = soup.select_one('.lst_detail_t1')
imgs = ul.find_all('img')
print(len(imgs))
for img in imgs:
    urls = img.get('src')
    title = img.get('src').split('/')[-2]
    filetype = title.split('_')[-1]
    title = title.split('_')[-2]
    req.urlretrieve(urls, moviedir + title+'.'+filetype)
