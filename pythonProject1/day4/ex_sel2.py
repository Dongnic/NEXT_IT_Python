from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = set_chrome_driver()
driver.implicitly_wait(3)
driver.get('https://www.msn.com/ko-kr/news/entertainment?cvid=91863bc9b5d640a9aa9a13c829b1ae06')

try:
    cnt = 10
    pagedown = 1
    body = driver.find_element(By.TAG_NAME,'body')
    while pagedown < cnt:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        pagedown += 1
        data = []
    # 스크롤을 내린 후 bs4 파싱하여
    # 기사 href 와 제목을 txt or csv로 저장하시오
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(driver.page_source,'html.parser')
    content = soup.select_one('.riverSections-DS-EntryPoint1-1')
    divs = content.select('.contentCard_headingContainer-DS-card1-1')
    for div in divs:
        a = div.select('a')
        title = a[1].text
        href = a[1].get('href')
        data.append([title,href])

    with open('news.csv','w',encoding='utf8') as f:
        write = csv.writer(f, delimiter='|',quotechar='"')
        for i in data:
                write.writerow(i)
except Exception as e:
    print(str(e))
driver.close()