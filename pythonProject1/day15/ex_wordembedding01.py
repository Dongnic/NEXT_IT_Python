import requests
import os
from gensim.models.word2vec import Word2Vec
import re
save_model = './book.model'
# 그림 형제의 동화
res = requests.get('https://www.gutenberg.org/files/2591/2591-0.txt')
grimm = res.text[2801:530661]
grimm = re.sub(r'[^a-zA-Z\.]',' ', grimm)
sentence = grimm.split('. ')
data = [s.split() for s in sentence]
print(data[0])
model = Word2Vec(data, sg=1 # 0:CBOW 주변단어로 타켓단어 예측, 1:Skip-gram 타켓단어로 주변
                 ,vector_size=200 #임베딩 벡터사이즈 (단어당 200차원)
                 ,window=3        # 주변 몇 번째 단어까지 볼껀지
                 ,min_count=3     # 최소 출현횟수
                 ,workers=4)       # 동시에 처리할 작업수

model.save(save_model)
while True:
    text1, text2 = input('비교 단어를 입력하시오(end=q):').split()
    if text1 == 'q':
        break
    else:
        print('positive:', model.wv.most_similar(positive=[text1, text2]))
        print('po:text1 ne:text2' , model.wv.most_similar(positive=[text1],negative=[text2]))
