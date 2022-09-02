from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
import logging, os
import math
import time
from collections import Counter

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import sqlite3
import numpy as np
import tensorflow as tf
import re
from keras.preprocessing.text import Tokenizer
from konlpy.tag import Mecab
from keras.utils import pad_sequences
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def search(keyword):
    token = np.load('model/vocab_token2.npy', allow_pickle=True)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(token)

    threshold = 2
    total_cnt = len(tokenizer.word_index)  # 단어의 수
    rare_cnt = 0  # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
    total_freq = 0  # 훈련 데이터의 전체 단어 빈도수 총 합
    rare_freq = 0  # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

    # 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
    for key, value in tokenizer.word_counts.items():
        total_freq = total_freq + value
        # 단어의 등장 빈도수가 threshold보다 작으면
        if (value < threshold):
            rare_cnt = rare_cnt + 1
            rare_freq = rare_freq + value

    vocab_size = total_cnt - rare_cnt + 2
    tokenizer = Tokenizer((vocab_size + 1), oov_token='OOV')
    tokenizer.fit_on_texts(token)
    model = tf.keras.models.load_model('model/ko_model01.h5')
    mecab = Mecab()

    max_len = 80
    stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯',
                 '지',
                 '임', '게']

    conn = sqlite3.connect('naver_map_url.db')
    cur = conn.cursor()
    query = """
                select re_contents from url_review where re_url = ?
            """
    insert_query = """
                insert into url_review
                    (re_writer, re_contents, re_date, re_url)
                values
                    (?, ?, ?, ?)
            """

    def set_chrome_driver():
        ch_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        return ch_driver

    option = webdriver.ChromeOptions()
    option.add_experimental_option("useAutomationExtension", False)
    option.add_experimental_option("excludeSwitches", ['enable-automation'])
    option.add_argument("start-maximized")
    option.add_argument("disable-infobars")
    option.add_argument("--disable-extensions")
    option.add_argument('user-agent=' +
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36')
    option.add_argument('--headless')

    def sentiment_predict(new_sentence):
        # new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', new_sentence)
        new_sentence = re.sub(r'[^가-힣 ]', '', new_sentence)
        print('정규화', new_sentence)
        noun = mecab.nouns(new_sentence)
        noun = mecab.nouns(new_sentence)
        p_noun = []
        for i in noun:
            if len(i) > 1:
                p_noun.append(i)
        print(p_noun)
        count = Counter(p_noun)
        # 명사 빈도 카운트
        noun_list = count.most_common(5)
        for v in noun_list:
            print(v)
        new_sentence = mecab.morphs(new_sentence)
        print('형태소 분석', new_sentence)
        new_sentence = [word for word in new_sentence if word not in stopwords]
        # 각 형태소 별 긍 부정 평가
        # for i in new_sentence:
        #     print(i)
        #     encoded = tokenizer.texts_to_sequences([i])
        #     pad_i = pad_sequences(encoded, maxlen=max_len)
        #     print('model.predict', float(model.predict(pad_i)))
        encoded = tokenizer.texts_to_sequences([new_sentence])
        print(encoded)
        pad_new = pad_sequences(encoded, maxlen=max_len)
        score = float(model.predict(pad_new))
        print(score)
        p_score = math.trunc(score * 10)
        print(p_score)
        if score > 0.98:
            return noun_list, "{:.2f} / 100점으로 <span style='color:lightgreen;'>맛집</span>입니다.".format((score * 10 - p_score) * 100)
        elif score > 0.95:
            return noun_list, "{:.2f} / 100점으로 <span style='color:blue;'>평범</span>합니다.".format((score * 10 - p_score) * 100)
        elif score > 0.90:
            return noun_list, "{:.2f} / 100점으로 <span style='color:orange;'>조심</span>하세요.".format((score * 10 - p_score) * 100)
        else:
            return noun_list, "<span style='color:red;'>웬만하면 가지마세요</span>"

    def geturl(keyword):
        driver = set_chrome_driver()
        if 'http' not in keyword:
            search_word = '대전%20' + keyword
            try:
                print(search_word)
                naver_url = f"https://m.map.naver.com/search2/search.naver?query={search_word}&sm=hty&style=v5"
                driver.get(naver_url)
                time.sleep(2)
                data_cid = driver.find_element(By.CSS_SELECTOR,
                                               "#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute(
                    'data-cid')
                # 네이버 지도 시스템은 data-cid에 url 파라미터를 저장해두고 있었습니다.
                # data-cid 번호를 뽑아두었다가 기본 url 템플릿에 넣어 최종적인 url을 완성하면 됩니다.
                # 만약 검색 결과가 없다면?
            except Exception as e1:
                if "li:nth-child(1)" in str(e1):  # -> "child(1)이 없던데요?"
                    try:
                        data_cid = driver.find_element(By.CSS_SELECTOR,
                                                       "#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview").get_attribute(
                            'data-cid')
                    except Exception as e2:
                        data_cid = 'none'
                else:
                    data_cid = 'none'
        else:
            driver.get(keyword)
            time.sleep(2)
            temp_cid = driver.current_url
            data_cid = temp_cid.split('?')[0].split('place/')[1]

        driver.close()
        print('data_cid', data_cid)
        if data_cid == 'none':
            return 'fail'
        else:
            naver_url = 'https://m.place.naver.com/restaurant/' + data_cid
            return naver_url

    def do_html_crawl(url: str):
        endcnt = 30  # 100개 / 늘릴때 마다 20개
        thr_driver = set_chrome_driver()
        thr_driver.set_window_size(500, 700)
        thr_driver.implicitly_wait(3)
        thr_driver.get(url + '/review/visitor')
        for i in range(1000000):
            # explicitly_wait
            if i == endcnt:
                break
            thr_driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            try:
                element = thr_driver.find_element(By.CSS_SELECTOR,
                                                  '#app-root > div > div > div div.place_section.lcndr > div.lfH3O > a'
                                                  )
                actions = ActionChains(thr_driver) \
                    .move_to_element(element) \
                    .click()
                actions.perform()  # actions 실행
                time.sleep(0.3)
            except Exception as e1:
                print(e1)
                break
        source = thr_driver.page_source
        review_list = []
        re_contents_list = []
        bs = BeautifulSoup(source, 'html.parser')
        li_element_tags = bs.select('.eCPGL li')
        for tag in li_element_tags:
            try:
                re_writer = tag.select_one('.sBWyy').text
            except Exception as e2:
                print(e2)
                re_writer = 'delete'
            try:
                re_contents = tag.select_one('div.ZZ4OK.IwhtZ > a > span').text
            except Exception as e2:
                print(e2)
                re_contents = 'delete'
            try:
                re_date = tag.select_one('div.sb8UA time').text
                if len(re_date) < 8:
                    re_date = '22.' + re_date
            except Exception as e2:
                print(e2)
                re_date = 'delete'
            re_url = url
            re_contents_list.append(re_contents)
            review_list.append((re_writer, re_contents, re_date, re_url))
        print('리뷰 갯수: ', len(review_list))
        cur.executemany(insert_query, review_list)
        conn.commit()
        # thr_driver.close()
        return re_contents_list

    url = geturl(keyword)
    if url == 'fail':
        most_word = ' '
        comment = '존재하지 않는 식당입니다. 다시 입력 해주세요'
    else:
        cur.execute(query, [url])
        rows = cur.fetchall()
        print(len(rows))
        if len(rows) > 0:
            most_word, comment = sentiment_predict(str(rows))
        else:
            print('리뷰가 없습니다. 재검색을 시도합니다.')
            search_data = do_html_crawl(url)
            print(search_data)
            most_word, comment = sentiment_predict(str(search_data))
    conn.close()
    return most_word, comment


@app.route('/')
def index():
    return render_template('index.html', name='Nick')


@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        keyword = request.form['test']
        most_word, comment = search(keyword)
        return {"most_word": most_word, "comment": comment}
    else:
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True, host="192.168.0.20", port=5555)
