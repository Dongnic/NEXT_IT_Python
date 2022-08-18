import re

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()  # 크롬 옵션 객체 생성
user_agent = "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36 "
options.add_argument('user-agent=' + user_agent)
options.add_argument('headless')  # headless 모드 설정
options.add_argument("window-size=1920x1080")  # 화면크기(전체화면)
options.add_argument("disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--mute-audio")  # mute
options.add_argument('--blink-settings=imagesEnabled=false')  # 브라우저에서 이미지 로딩을 하지 않습니다.
options.add_argument('incognito')  # 시크릿 모드의 브라우저가 실행됩니다.
options.add_argument("--start-maximized")

# 1
prefs = {
    "translate_whitelists": {"en": "ko"},
    "translate": {"enabled": "true"}
}
options.add_experimental_option("prefs", prefs)

# 2
prefs = {
    "translate_whitelists": {"your native language": "ko"},
    "translate": {"enabled": "True"}
}
options.add_experimental_option("prefs", prefs)

# 3
options.add_experimental_option('prefs', {'intl.accept_languages': 'ko,ko_kr'})

import os
import pandas as pd
import winsound

ytb = pd.read_csv('youtube_link.csv')
ytb_link = ytb.link.to_list()

for i in ytb_link:
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get(i)

    # 스크롤 다운
    time.sleep(1.5)
endkey = 4  # 90~120개 / 늘릴때 마다 30개
while endkey:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(0.3)
    endkey -= 1

channel_name = driver.find_element_by_xpath('//*[@id="text-container"]').text
subscribe = driver.find_element_by_css_selector('#subscriber-count').text
channel_name = re.sub('[=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…《\》]', '', channel_name)
# print(channel_name,subscribe)

# bs4 실행
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

video_list0 = soup.find('div', {'id': 'contents'})
video_list2 = video_list0.find_all('ytd-grid-video-renderer', {'class': 'style-scope ytd-grid-renderer'})

base_url = 'https://www.youtube.com'
video_url = []

# 반복문을 실행시켜 비디오의 주소를 video_url에 넣는다.
for i in range(len(video_list2)):
    url = base_url + video_list2[i].find('a', {'id': 'thumbnail'})['href']
    video_url.append(url)

driver.quit()

if subscribe:
    channel = channel_name + ' - ' + subscribe
else:
    channel = channel_name

directory = f'data/{channel}/subtitle'
if not os.path.exists(directory):
    os.makedirs(directory)

print(channel, len(video_url))

ytb_info(video_url, channel)
print()
