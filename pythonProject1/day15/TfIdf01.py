import pandas as pd # 데이터프레임 사용을 위해
from math import log # IDF 계산을 위해

# TF-IDF(Term Frequency-Inverse Document Frequency)는
# tf(d,t) : 특정 문서 d에서의 특정 단어 t의 등장 횟수.
# df(t) : 특정 단어 t가 등장한 문서의 수.
# idf(d, t) : df(t)에 반비례하는 수.

# 단어의 빈도와 역 문서 빈도(문서의 빈도에 특정 식을 취함)를 사용하여
# DTM(Document-Term Matrix 다수의 문서에서 등장하는 각 단어들의 빈도를 행렬로 표현한 것)
# 내의 각 단어들마다 중요한 정도를 가중치로 주는 방법입니다.
# 사용 방법은 우선 DTM을 만든 후, TF-IDF 가중치를 부여합니다.

docs = ['이 제품의 용도는 졸업 선물이다. 이 제품의 용도는 졸업선물 외에도 가능하다.'
       ,'이 제품의 용도는 세안이다. 이 제품의 용도는 세안 외에도 여러 용도를 정할 수 있다.'
       ,'이 제품의 용도는 간식이다. 이 제품의 용도는 간식 외에도 용도를 정할 수 있다.']

vocab = list(set(w for doc in docs for w in doc.split()))
vocab.sort()

N = len(docs) # 총 문서의 수

def tf(t, d):
    return d.count(t)

def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df + 1))

def tfidf(t, d):
    return tf(t,d) * idf(t)

# tf(d,t) : 특정 문서 d에서의 특정 단어 t의 등장 횟수.
result = []
for i in range(N): # 각 문서에 대해서 아래 명령을 수행
    result.append([])
    d = docs[i]
    for j in range(len(vocab)):
        t = vocab[j]
        result[-1].append(tf(t, d))

tf_ = pd.DataFrame(result, columns = vocab)
print('tf:', tf_)

#  df(t) : 특정 단어 t가 등장한 문서의 수.
# idf(d, t) : df(t)에 반비례하는 수.
result = []
for j in range(len(vocab)):
    t = vocab[j]
    result.append(idf(t))

idf_ = pd.DataFrame(result, index = vocab, columns=["IDF"])
print('idf:', idf_)

result = []
for i in range(N):
    result.append([])
    d = docs[i]
    for j in range(len(vocab)):
        t = vocab[j]
        result[-1].append(tfidf(t,d))

tfidf_ = pd.DataFrame(result, columns=vocab)
print('tf-idf:', tfidf_)

import numpy as np

def cosine_similarity(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

doc_list = tfidf_.values.tolist()
# 0 번째 문서와 가까운건 ?
while True:
    num = int(input("가까운 문서 찾기"))
    for i in range(len(doc_list)):
        if i != num:
            print(i, '번째 문서 유사도:', cosine_similarity(doc_list[num], doc_list[i]))