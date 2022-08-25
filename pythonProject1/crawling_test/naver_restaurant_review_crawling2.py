import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer  # 피체 벡터화
from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도
df = pd.read_csv('csv/url_data.csv')
print(df.info())

df = df[df['naver_map_url'].isnull()]
print(df.info())




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
df['naver_keyword'] = df['dong'] + "%20" + df['name_1']  # "%20"는 띄어쓰기를 의미합니다.
# 네이버 지도 검색창에 [~동 @@식당]으로 검색해 정확도를 높여야 합니다. 검색어를 미리 설정해줍시다.
# 본격적으로 가게 상세페이지의 URL을 가져옵시다
import sqlite3
con = sqlite3.connect("naver_map_url.db")
for i, keyword in enumerate(df['naver_keyword'].tolist()):
    print("이번에 찾을 키워드 :", i, f"/ {df.shape[0] - 1} 행", keyword)
    try:
        naver_map_search_url = f"https://m.map.naver.com/search2/search.naver?query=대전%20{keyword}&sm=hty&style=v5"

        driver.get(naver_map_search_url)
        time.sleep(2)
        df.iloc[i, -1] = driver.find_element(By.CSS_SELECTOR,
            "#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute(
            'data-cid')
        # 네이버 지도 시스템은 data-cid에 url 파라미터를 저장해두고 있었습니다.
        # data-cid 번호를 뽑아두었다가 기본 url 템플릿에 넣어 최종적인 url을 완성하면 됩니다.
        # 만약 검색 결과가 없다면?
    except Exception as e1:
        if "li:nth-child(1)" in str(e1):  # -> "child(1)이 없던데요?"
            try:
                df.iloc[i, -1] = driver.find_element(By.CSS_SELECTOR,
                    "#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute(
                    'data-cid')
                time.sleep(2)
            except Exception as e2:
                print(e2)
                df.iloc[i, -1] = np.nan
                time.sleep(2)
        else:
            pass
    finally:
        cur = con.cursor()
        query = """
                    update url_data
                    set (naver_map_url, naver_keyword) = (?, ?)
                    where lat == ?
                """
        cur.execute(query, (df.iloc[i, -1], df.iloc[i, 12], df.iloc[i, 10]))
        con.commit()
driver.quit()


# URL이 수집되지 않은 데이터는 제거합니다.
# df = df.loc[~df['naver_map_url'].isnull()]
# 이때 수집한 것은 완전한 URL이 아니라 URL에 들어갈 ID (data-cid 라는 코드명으로 저장된) 이므로, 온전한 URL로 만들어줍니다
# df['naver_map_url'] = "https://m.place.naver.com/restaurant/" + df['naver_map_url']
# df.to_sql("url_data", con, if_exists="replace", chunksize=1000)
# con.commit()
con.close()