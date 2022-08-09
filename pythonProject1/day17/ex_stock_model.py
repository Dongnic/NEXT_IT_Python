import pandas as pd
import numpy as np
from keras.layers import Dropout
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt


df = pd.read_excel('./005930.xlsx', engine='openpyxl')
data = df['Close']
print(data.head())
scaler = MinMaxScaler(feature_range=(0, 1))
s_data = scaler.fit_transform(np.array(data).reshape(-1, 1))
train_size = int(len(s_data) * 0.8)
test_size = len(s_data) - train_size
train_data, test_data = s_data[0:train_size, :], s_data[train_size:len(s_data), :1]
# 50일씩
time_step = 50


def fn_dataset(p_data, step=1):
    data_x, data_y = [], []
    for i in range(len(p_data) - step - 1):
        data_x.append(p_data[i:(i + step), 0])
        data_y.append(p_data[i + step, 0])
    return np.array(data_x), np.array(data_y)


x_train, y_train = fn_dataset(train_data, time_step)
x_test, y_test = fn_dataset(test_data, time_step)
print(x_train)
model = Sequential()
model.add(LSTM(150, return_sequences=True, input_shape=(time_step, 1)))
model.add(Dropout(0.2))
model.add(LSTM(150, return_sequences=True))
model.add(LSTM(64, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse', optimizer='adam')
model.summary()
monitor = EarlyStopping(monitor='val_loss', min_delta=1e-3, patience=30, verbose=1, mode='auto', restore_best_weights=True)
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), callbacks=[monitor], verbose=1, epochs=30)
model.save('samsung.model')
fig = plt.figure(facecolor='white', figsize=(20, 10))
ax = fig.add_subplot(111)
ax.plot(y_test, label='True')
pred = model.predict(x_test)
ax.plot(pred, label='prediction')
ax.legend()
plt.show()