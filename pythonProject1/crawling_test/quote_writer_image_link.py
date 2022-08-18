# 유동준
import re

from mydb import Mydb
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
db = Mydb()
option = webdriver.ChromeOptions()
# option.add_argument("headless")
option.add_argument('user-agent='+
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')

sql = """
    SELECT DISTINCT writer
    FROM quotes
    """
text = db.get_select(sql)
w_list = []
cnt = 1
for i in text:
    cnt += 1
    w_list.append(list(i))
not_found_list = []


def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    return driver


def split_list(link):
    half = len(link)//2
    return link[:half], link[half:]


def fn_crawling_image_link():
    cnt1 = 0
    for list in w_list:
        link = "no"
        print("---------------------------------------------------------------------------------------------")
        print(list[0])
        url = 'https://ko.wikipedia.org/wiki/{0}'.format(str(list[0]))
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(soup.prettify())
        # img_src = soup.select_one('.infobox > tbody > tr:nth-child(2) > td > a > img')['src']
        tbody = soup.select_one('.infobox > tbody')
        if tbody:
            try:
                src = tbody.select_one('tr:nth-child(2) > td > a > img')['src']
                if src:
                    link = "https:"+src
                else:
                    not_found_list.append(str(list[0]))
            except TypeError:  # 예외가 발생했을 때 실행됨
                print('타입 에러 예외가 발생했습니다.')
                not_found_list.append(str(list[0]))
        else:
            tbody = soup.select_one('.thumbinner')
            if tbody:
                src = tbody.select_one('a > img')['src']
                if src:
                    link = "https:"+src
                else:
                    not_found_list.append(str(list[0]))
            else:
                not_found_list.append(str(list[0]))
        if link != 'no':
            print(link)
            # 쿼리 넣기
            insert_sql = """
                                 UPDATE
                                /*+ bypass_ujvc */
                                (   SELECT img1, writer
                                    FROM quotes a
                                    WHERE writer = :1
                                )
                                SET img1 = :2
                                 """
            cnt1 += db.fn_insert(insert_sql, [list[0], link])
            print(cnt1, '건 삽입')
            cnt1 += 1
        # if not_found_list:
        #     print(not_found_list)
        print("---------------------------------------------------------------------------------------------")
    print('위키 총', cnt1, '건 삽입')


def fn_not_image_link():
    cnt2 = 0
    for loser in not_found_list:
        url = 'https://www.google.com/search?q='
        driver = set_chrome_driver()
        driver.implicitly_wait(1)
        driver.get(url + loser)
        driver.implicitly_wait(1)
        # driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
        try:
            img_div = driver.find_element(By.CLASS_NAME, 'SzZmKb')
            if img_div:
                try:
                    if img_div.find_element(By.TAG_NAME, 'g-img') is not None:
                        g_img = img_div.find_element(By.TAG_NAME, 'g-img')
                        if g_img.find_element(By.TAG_NAME, 'img').get_attribute('src') is not None:
                            link = g_img.find_element(By.TAG_NAME, 'img').get_attribute('src')
                        link1, link2 = split_list(link)
                        print(link1 + link2, loser)
                        # 쿼리 넣기
                        insert_sql = """
                                        UPDATE quotes
                                        SET img1 = :1, img2 = :2
                                        WHERE writer = :3
                                     """
                        cnt2 += db.fn_insert(insert_sql, [link1, link2, loser])
                        print(cnt2, '건 삽입')
                except Exception:
                    coadsnk = 1
        except Exception:
            coadsnk = 1
        driver.close()
    print('구글 총', cnt2, '건 삽입')


fn_crawling_image_link()
fn_not_image_link()