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
df = pd.read_csv('csv/url_data.csv')
# urls = df['naver_map_url'].values
urls = [
    'https://m.place.naver.com/restaurant/1341510805',
    'https://m.place.naver.com/restaurant/1225486920',
    'https://m.place.naver.com/restaurant/1721900132',
    'https://m.place.naver.com/restaurant/16114704',
    'https://m.place.naver.com/restaurant/1937113082',
    'https://m.place.naver.com/restaurant/30936508',
    'https://m.place.naver.com/restaurant/1066651732',
    'https://m.place.naver.com/restaurant/36255454',
    'https://m.place.naver.com/restaurant/19611306',
    'https://m.place.naver.com/restaurant/37852583',
    'https://m.place.naver.com/restaurant/16075169',
    'https://m.place.naver.com/restaurant/1929418256',
    'https://m.place.naver.com/restaurant/1231853596',
    'https://m.place.naver.com/restaurant/16054413',
    'https://m.place.naver.com/restaurant/13454364',
    'https://m.place.naver.com/restaurant/32216036',
    'https://m.place.naver.com/restaurant/16059211',
    'https://m.place.naver.com/restaurant/1354346224',
    'https://m.place.naver.com/restaurant/21447318'
]
limit = 100
result_list = []
option = webdriver.ChromeOptions()
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
    driver = set_chrome_driver()
    driver.implicitly_wait(3)
    # explicitly_wait
    review_list = []
    endcnt = 5  # 100개 / 늘릴때 마다 20개
    for i in range(1000000):
        driver.get(url+'/review/visitor')
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        element = driver.find_element(By.CSS_SELECTOR,
            '#app-root > div > div > div > div:nth-child(7) > div:nth-child(2) > div.place_section.lcndr > div.lfH3O > a'
        )
        actions = ActionChains(driver) \
            .move_to_element(element) \
            .click()
        actions.perform()  # actions 실행
        time.sleep(0.3)
        endcnt -= 1
        if i == endcnt:
            break
    source = driver.page_source
    bs = BeautifulSoup(source, 'html.parser')
    li_element_tags = bs.find_all('li', attrs={'class': 'YeINN'})
    for tag in li_element_tags:
        for span in tag.find('div:nth-child(2) span.zPfVt'):
            review_list.append(span.text())

    driver.close()
    review_list = review_list[:limit]
    print('리뷰 길이: ', len(review_list))
    return review_list


def do_thread_crawl(urls: list):
    with ThreadPoolExecutor(max_workers=8) as executor:
        thread_list = []
        for url in urls:
            thread_list.append(executor.submit(do_html_crawl, url))
            print(thread_list)
        for execution in concurrent.futures.as_completed(thread_list):
            result = execution.result()
            print(result)
            result_list.append(result)


if __name__ == "__main__":
    start_time = time.time()
    do_thread_crawl(urls)
    print(result_list)
    print("--- elapsed time %s seconds ---" % (time.time() - start_time))