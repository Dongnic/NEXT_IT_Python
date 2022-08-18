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
    endk -= 1

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
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
