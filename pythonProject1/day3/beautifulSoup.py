# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests as req

def fn_write_txt(text):

    f = open('movie_info.txt', 'a')
    f.write(text)
    f.writelines('\n')
    f.close()
for i in range(1, 50):
    url = 'https://movie.naver.com/movie/point/af/list.naver?&page='+str(i)
    resp = req.get(url)
    # print(resp)
    print(resp.text)
    soup = bs(resp.text, 'html.parser')
    # print(soup) 구조화 되게 출력
    # prettify() 보기좋게
    print(soup.prettify())
    table = soup.select_one('.list_netizen')
    print(table)
    trs = table.find_all('tr')
    page = 1
    for tr in trs:
        a = tr.select_one('.title a')
        if a:
            title = a.text
            url = a.get('href')
            em = tr.select_one('.list_netizen_score em')
            score = em.text
            print("[", title, "]", "\n평점 : ", score, " [링크 : ", url, "]", sep="")
            td = tr.select_one('.title')
            text_tag = str(td).split('<br/>')
            if len(text_tag) > 1:
                msg = text_tag[1].split('\n')
                reply = msg[0].strip()
            else:
                pass
            user = tr.select_one('.author').text
            print('제목:', title, '영화평가:', reply, '평점:', score, '상세정보:', url, 'id:', user)
            aaa = tr.find_all('td')[2]
            data_tag = str(tr.find_all('td')[2]).split('<br/>')
            if len(data_tag) > 1:
                date = data_tag[1].replace('</td>', '')
            #fomat
            info = "[{6}]\n[{0}] 평점 : {1}\n영화평가 : {2}\nID : {3}\n영화상세정보 : {4}\n작성일 : {5}\n".format(
                title, score, reply, user, url, date, ((i-1)*10)+page)
            page += 1
            fn_write_txt(info)
        # print(trs)
