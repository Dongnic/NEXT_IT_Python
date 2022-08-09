import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler


model = load_model('./samsung.model')
df = pd.read_excel('./005930_20220525_20220804.xlsx')
data = df['Close'].values
scaler = MinMaxScaler(feature_range=(0, 1))
s_data = scaler.fit_transform(np.array(data).reshape(-1, 1))
test_data = np.ravel(s_data, order='C')
test_data = np. array([test_data])
y_pred = model.predict(test_data)
print('마지막 날', test_data[0][-1])
print('오늘 예측', y_pred)
print(scaler.inverse_transform(np.array(test_data[0][-1]).reshape(-1, 1)), ' won')
print(scaler.inverse_transform(np.array(y_pred[0]).reshape(-1, 1)), ' won')