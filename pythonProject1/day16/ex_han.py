# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from day5 import mydb
import re

db = mydb.Mydb()

# for code in fn_getcode():
url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=194196'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
movielist = []
# 구조화 되게 출력
try:
    title = soup.select_one('.h_movie> a').text
    category = soup.select_one(
        "#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a").text
    year = soup.select_one(
        "#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)").text.split(
        '.')[0].replace('\n', '')
    actor = soup.select_one(
        "#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p > a:nth-child(1)").text
    screen_time = soup.select_one(
        "#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)").text
    score = soup.select_one(".spc .star_score").text.replace('\n', '')
    movielist.append([title, category, year, actor, screen_time, score])
    if movielist is not None:
        print(movielist)
        sql = """
        INSERT INTO movie (
          mv_no
        , title
        , mv_category
        , mv_year
        , actor
        , screen_time
        , score
        ) VALUES (
        movie_seq.nextval
        , :1
        , :2
        , :3
        , :4
        , :5
        , :6
        )
        """
        cnt = db.fn_insert(sql, [movielist[0][0], movielist[0][1], movielist[0][2],
                            movielist[0][3], movielist[0][4], movielist[0][5]])
except Exception as e:
    print(e)