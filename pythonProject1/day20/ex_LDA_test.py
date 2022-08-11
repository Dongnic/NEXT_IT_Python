from gensim.models import LdaModel
from gensim.corpora import Dictionary
from konlpy.tag import Okt
import os
okt = Okt()
def fn_test(model, dictionary, doc):
    text = okt.nouns(doc)
    words = []
    for word in text:
        if len(word) > 1:
            words.append(word)
    test = model[dictionary.doc2bow(words)]
    result = sorted(test, key=lambda x : x[1], reverse=True)
    print(result)
model = LdaModel.load('./model/lda_new.model')
topic = model.print_topics(num_topics=8, num_words=15)
for i in topic:
    print(i)
word_dictionary = Dictionary.load_from_text('./model/model.dictionary')
path = '../day15/newsData/5/'
file_list = os.listdir(path)
for file in file_list:
    with open(path + file, 'r', encoding='utf-8') as f:
        data = f.read()
        fn_test(model, word_dictionary, data)