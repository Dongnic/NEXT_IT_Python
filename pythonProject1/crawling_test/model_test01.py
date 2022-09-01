import logging, os

from sklearn.model_selection import train_test_split

logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
import tensorflow as tf
import numpy as np
import re
from konlpy.tag import Mecab
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import pandas as pd
stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하', '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯', '지', '임', '게']
mecab = Mecab()
total_data = pd.read_table('model/naver_shopping.txt', names=['ratings', 'reviews'])
total_data['label'] = np.select([total_data.ratings > 3], [1], default=0)
total_data['ratings'].nunique(), total_data['reviews'].nunique(), total_data['label'].nunique()
total_data.drop_duplicates(subset=['reviews'], inplace=True) # reviews 열에서 중복인 내용이 있다면 중복 제거
print('총 샘플의 수 :',len(total_data))
train_data, test_data = train_test_split(total_data, test_size = 0.2, random_state = 42)
print('훈련용 리뷰의 개수 :', len(train_data))
print('테스트용 리뷰의 개수 :', len(test_data))
train_data['reviews'] = train_data['reviews'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", regex=True)
train_data['reviews'].replace('', np.nan, inplace=True)
print(train_data.isnull().sum())
train_data['tokenized'] = train_data['reviews'].apply(mecab.morphs)
train_data['tokenized'] = train_data['tokenized'].apply(lambda x: [item for item in x if item not in stopwords])
X_train = train_data['tokenized'].values
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)

threshold = 2
total_cnt = len(tokenizer.word_index) # 단어의 수
rare_cnt = 0  # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
total_freq = 0  # 훈련 데이터의 전체 단어 빈도수 총 합
rare_freq = 0  # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

# 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
for key, value in tokenizer.word_counts.items():
    total_freq = total_freq + value
    # 단어의 등장 빈도수가 threshold보다 작으면
    if(value < threshold):
        rare_cnt = rare_cnt + 1
        rare_freq = rare_freq + value

vocab_size = total_cnt - rare_cnt + 2
print(vocab_size)
tokenizer = Tokenizer(vocab_size, oov_token='OOV')
np.save('model/vocab_token2.npy', X_train)
print(type(X_train))
tokenizer.fit_on_texts(X_train)
max_len = 80
model = tf.keras.models.load_model('model/ko_model01.h5')


def sentiment_predict(new_sentence):
    print(new_sentence)
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]', '', new_sentence)
    print(new_sentence)
    new_sentence = mecab.morphs(new_sentence)
    print(new_sentence)
    new_sentence = [word for word in new_sentence if word not in stopwords]
    print(new_sentence)
    encoded = tokenizer.texts_to_sequences([new_sentence])
    encoded2 = tokenizer.texts_to_sequences(['I have dog'])
    print(encoded)
    print(encoded2)
    pad_new = pad_sequences(encoded, maxlen=max_len)
    print(pad_new)
    score = float(model.predict(pad_new))
    print(score)
    if(score > 0.5):
        print("{:.2f}% 확률로 긍정 리뷰입니다.".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.".format((1 - score) * 100))


sentiment_predict('좋아')
