from sklearn.feature_extraction.text import TfidfVectorizer

doc =['이 제품의 용도는 졸업 선물이다. 이 제품의 용도는 졸업 선물 외에도 가능하다.'
      ,'이 제품의 용도는 세안이다. 이 제품의 용도는 세안 외에도 여러 용도를 정할 수 있다.'
      , '이 제품의 용도는 간식이다. 이 제품의 용도는 간식 외에도 용도를 정할 수 있다.']

tfidfv = TfidfVectorizer().fit(doc)
print('array',tfidfv.transform(doc).toarray())
print('vocabulary_',tfidfv.vocabulary_)
sorted(tfidfv.vocabulary_.items())

docs = tfidfv.fit_transform(doc)
distaince = docs * docs.T
print(docs)
print(distaince.toarray())