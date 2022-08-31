from fake_useragent import UserAgent
from time import sleep
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from selenium import webdriver
import concurrent.futures
import urllib.request
import requests
import time
import pandas as pd
import numpy as np
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3
query = """
            insert into url_review
                (re_writer, re_contents, re_date, re_url)
            values
                (?, ?, ?, ?)
        """
df = pd.read_csv('csv/url_data2.csv')
urls = df['naver_map_url'].values
result_list = []
option = webdriver.ChromeOptions()
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument("start-maximized")
option.add_argument("disable-infobars")
option.add_argument("--disable-extensions")
option.add_argument('user-agent='+
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')
# option.add_argument('--headless')


def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    return driver


def do_html_crawl(url: str):
    endcnt = 30  # 100개 / 늘릴때 마다 20개
    driver.implicitly_wait(3)
    driver.get(url+'/review/visitor')
    for i in range(1000000):
        # explicitly_wait
        if i == endcnt:
            break
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        try:
            element = driver.find_element(By.CSS_SELECTOR,
                '#app-root > div > div > div div.place_section.lcndr > div.lfH3O > a'
            )
            actions = ActionChains(driver) \
                .move_to_element(element) \
                .click()
            actions.perform()  # actions 실행
            time.sleep(0.5)
        except Exception as e1:
            print(e1)
            break
    source = driver.page_source
    review_list = []
    bs = BeautifulSoup(source, 'html.parser')
    li_element_tags = bs.select('.eCPGL li')
    for tag in li_element_tags:
        print('태그 이름: ', tag)
        try:
            re_writer = tag.select_one('.sBWyy').text
            print(re_writer)
        except Exception as e2:
            print(e2)
            re_writer = 'delete'
        try:
            re_contents = tag.select_one('div.ZZ4OK.IwhtZ > a > span').text
            print(re_contents)
        except Exception as e2:
            print(e2)
            re_contents = 'delete'
        try:
            re_date = tag.select_one('div.sb8UA time').text
            print(re_date)
            if len(re_date) < 8:
                re_date = '22.' + re_date
        except Exception as e2:
            print(e2)
            re_date = 'delete'
        re_url = url
        print(url)
        review_list.append((re_writer, re_contents, re_date, re_url))
    print('리뷰 갯수: ', len(review_list))
    cur.executemany(query, review_list)
    conn.commit()


def do_thread_crawl(urls: list):
    for url in urls:
        cur.execute("""SELECT count(*) FROM url_review WHERE re_url = ? """, [url])
        cnt = cur.fetchone()
        print(cnt[0])
        if cnt[0] < 1:
            do_html_crawl(url)


if __name__ == "__main__":
    start_time = time.time()
    conn = sqlite3.connect('naver_map_url.db')
    cur = conn.cursor()
    driver = set_chrome_driver()
    driver.set_window_size(500, 700)
    do_thread_crawl(urls)
    driver.close()
    conn.close()
    print(result_list)
    print("--- elapsed time %s seconds ---" % (time.time() - start_time))