from gensim.models.word2vec import Word2Vec

model = Word2Vec.load('./movie.model')
print(model.wv.most_similar(positive=['한산']))