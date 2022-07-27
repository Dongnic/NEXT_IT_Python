import sys
import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# seed 값 설정 (똑같은 랜덤 값 나오도록)
tf.random.set_seed(0)

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 학습을 위해 데이터 구조 변형
x_train = x_train.reshape(x_train.shape[0], 784).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 784).astype('float32') / 255
# 정답 숫자를 Labeling
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
model = Sequential()
model.add(Dense(512, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
# model.fit(x_train, y_train, epochs=30, batch_size=200)
# model.save('first_model.model')
# 모델 저장
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)
modelpath = './model/{epoch:02d}-{val_loss:.4f}.hdf5'
from keras.callbacks import ModelCheckpoint, EarlyStopping
checkpoint = ModelCheckpoint(filepath=modelpath, monitor='val_loss'
                             , verbose=1, save_best_only=True)
# 10회 이상 동일하면 멈춤
early_stop = EarlyStopping(monitor='val_loss', patience=10)
history = model.fit(x_train, y_train, epochs=30
          , batch_size=200
          , validation_data=(x_test, y_test)
          , callbacks=[early_stop, checkpoint])
# 테스트 정확도 출력
print('\n test acc: %.4f' % model.evaluate(x_test, y_test)[1])
# 테스트 셋 오차
y_test_loss = history.history['val_loss']
# 학습데이터 오차
y_loss = history.history['loss']
# 그래프로 표현
xlen = np.arange(len(y_loss))
plt.plot(xlen, y_test_loss, marker='.', c='red', label='test loss')
plt.plot(xlen, y_loss, marker='.', c='blue', label='train loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()