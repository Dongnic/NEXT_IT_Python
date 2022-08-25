# 본격 네이버 리뷰 크롤링
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


def set_chrome_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    return driver


option = webdriver.ChromeOptions()
# option.add_argument("headless")
option.add_argument('user-agent='+
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')
driver = set_chrome_driver()
naver_map_search_url = "https://m.map.naver.com/search2/search.naver?query=유천1동 이현주나주곰탕&sm=hty&style=v5"

driver.get(naver_map_search_url)
time.sleep(1)
naver_url = driver.find_element(By.CSS_SELECTOR,
    "#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute(
    'data-cid')

driver.quit()
print(naver_url)