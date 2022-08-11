import os
import gensim
from konlpy.tag import Okt

root = '../day15/newsData/'
docs_ko = []
dirs = ['1', '5', '6']
for dir in dirs:
    if os.path.isdir(root + dir):
        files = os.listdir(root + dir)
        for file in files:
            with open(root + dir + '/' + file, 'r', encoding='utf-8') as f:
                doc = f.read()
                docs_ko.append(doc)
print(docs_ko)
okt = Okt()
docs = []
for line in docs_ko:
    nouns = okt.nouns(line)
    tokens = []
    for word in nouns:
        if len(word) > 1:
            tokens.append(word)
    docs.append(tokens)
print(docs)
from gensim import corpora
word_dictionary = corpora.Dictionary(docs)
word_dictionary.save_as_text('./model/model.dictionary')
corpus = [word_dictionary.doc2bow(text) for text in docs]
model = gensim.models.ldamodel.LdaModel(corpus
                                        ,num_topics=3
                                        ,id2word=word_dictionary
                                        ,passes=200)
model.save('./model/lda_new.model')
print(model)
topic = model.print_topics(num_topics=8, num_words=10)
for i in topic:
    print(i)