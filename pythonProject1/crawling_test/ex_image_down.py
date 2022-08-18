import urllib.request
from mydb import Mydb
import splitfolders
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

db = Mydb()
option = webdriver.ChromeOptions()
# option.add_argument("headless")
option.add_argument('user-agent='+
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')

url = 'https://www.google.com/search?q='
not_found_list = ['J.M. 싱', '빌헬름 뮐러', '오르데카', '로저스']


def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    return driver


def split_list(link):
    half = len(link)//2
    return link[:half], link[half:]

def fn_not_image_link():
    cnt2 = 0
    for loser in not_found_list:
        url = 'https://www.google.com/search?q='
        driver = set_chrome_driver()
        driver.implicitly_wait(1)
        driver.get(url + loser)
        driver.implicitly_wait(1)
        # driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

        img_div = driver.find_element(By.CLASS_NAME, 'SzZmKb')
        if img_div:
            try:
                if img_div.find_element(By.TAG_NAME, 'g-img') is not None:
                    g_img = img_div.find_element(By.TAG_NAME, 'g-img')
                    if g_img.find_element(By.TAG_NAME, 'img').get_attribute('src') is not None:
                        link = g_img.find_element(By.TAG_NAME, 'img').get_attribute('src')
                    print(link)
                    link1, link2 = split_list(link)
                    print(link1 + link2, loser)
                    print("---------------------------------------------------------------------------------------------")
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
        driver.close()
    print('총', cnt2, '건 삽입')
