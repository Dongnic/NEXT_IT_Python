# pip install selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

url = 'http://tour.interpark.com/'
driver = set_chrome_driver()
driver.implicitly_wait(3)
driver.get(url)
#접속 후 페이지가 다 로드되도록 딜레이
time.sleep(1)

driver.find_element(By.ID, 'SearchGNBText').send_keys('하와이')
driver.find_element(By.CLASS_NAME, 'search-btn').click()
time.sleep(2)
lis = driver.find_elements(By.CSS_SELECTOR, 'li.boxItem')
for li in lis:
    print(li.get_attribute('innerHTML'))
    text = li.text
    print(text)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())
driver.close()