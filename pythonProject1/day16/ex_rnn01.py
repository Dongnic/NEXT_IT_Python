docs = ["너무 재밌네요"
        ,"최고에요"
        ,"참 잘 만든 영화 입니다."
        ,"추천하고 싶은 영화 입니다"
        ,"한번 더 보고싶다"
        ,"별루"
        ,"재미없다"
        ,"지루하다"
        ,"재미없어요"
        ,"글쎄"]
# 긍정 1, 부정 0

import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, Embedding
from keras.preprocessing.text import text_to_word_sequence

target = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)
x = token.texts_to_sequences(docs)
print('토큰:', x)

# 패딩
pad = pad_sequences(x, 4)
print(pad)

# 임베딩에 사용될 단어 수
word_size = len(token.word_index) + 1
model=Sequential()
model.add(Embedding(word_size, 8, input_length=4))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(pad, target, epochs=20)
print('\n acc : %.4f' %(model.evaluate(pad, target)[1]))