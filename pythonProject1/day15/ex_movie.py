# -*- coding:utf-8 -*- 윈도우에서 인코딩 할때
from bs4 import BeautifulSoup
import requests

def fn_write_txt(text):

    f = open('movie_info.txt', 'a')
    f.write(text)
    f.writelines('\n')
    f.close()

for i in range(1, 1000):

    url = 'https://movie.naver.com/movie/point/af/list.naver?&page=1'+str(i)
    resp = requests.get(url)
    #print(resp)
    #print(resp.text)
    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(soup)
    # 구조화 되게 출력
    #print(soup.prettify())
    table = soup.select_one('.list_netizen')
    #print(table)
    trs = table.find_all('tr')
    # 제목, 평점, 상세url, 댓글
    for tr in trs:
        a= tr.select_one('.title a')


        if a:
            title = a.text
            url = a.get('href')
            em = tr.select_one('.list_netizen_score em')
            score = em.text

            td = tr.select_one('.title')
            text_tag = str(td).split('<br/>')
            if len(text_tag) > 1:
                msg = text_tag[1].split('\n')
                reply = msg[0].strip()
            else:
                pass
            user = tr.select_one('.author').text
            aaa = tr.find_all('td')[2]
            
            date_tag = str(tr.find_all('td')[2]).split('<br/>')
            if len(date_tag) > 1:
                date = date_tag[1].replace('</td>','')
            # format
            info = "제목: {0}평점:  {1}영화평가:    {2}평가자ID:   {3}영화상세정보:  {4}작성일: {5}".format(
                )
            #print(info)
            fn_write_txt(info)


