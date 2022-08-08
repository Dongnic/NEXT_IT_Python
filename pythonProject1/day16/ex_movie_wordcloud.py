# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from day5 import mydb
import re

def fn_sexy():
    for i in range(1000):
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page={0}'.format(str(i))
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        db=mydb.Mydb()
    # 구조화 되게 출력
        table = soup.select_one('.list_netizen')
        trs = table.find_all('tr')
        movie_reply = []
        for tr in trs:
            a = tr.select_one('.title a')
            if a:
                title = a.text
                url = a.get('href')
                num = tr.select_one('.ac').text
                code = url.split('&')[1]
                em = tr.select_one('.list_netizen_score em')
                score = em.text
                revi = tr.select_one('.title')
                revie = str(revi).split('<br/>')
                if len(revie) >1:
                    review = revie[1].split('\n')
                    reply = review[0].strip()
                else:
                    pass
                td2 = tr.select_one('.num:last-child')
                text_tag2 = str(td2).split('<br/>')
                if len(text_tag2) > 1:
                    date = text_tag2[1].split('<')
                    if len(date) > 1:
                        day = re.sub(r'[^0-9.]', '', date[0])

                movie_reply.append([num, title, code, score, reply, day])

        cnt = db.fn_insert_list("""INSERT INTO movie_reply (mv_num, mv_title, mv_code, mv_score, mv_reply, mv_date
                        ) VALUES (:1, :2, :3, :4, :5, :6)""", movie_reply)
    print(cnt, '건 저장')


fn_sexy()