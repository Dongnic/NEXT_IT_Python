import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('./datasets/streeteasy/manhattan.csv')
print(df.info())
print(df.describe())
print(df.columns)
x = df[['bedrooms', 'bathrooms', 'size_sqft',
       'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck',
       'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher',
       'has_patio', 'has_gym']]
y = df[['rent']]
print(x.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
# train : 8, test : 2
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

model = LinearRegression()
model.fit(x_train.values, y_train.values)
print(model.coef_)       # 기울기
print(model.intercept_)  # y절편
# 학습 데이터 정확도
model.score(x_train.values, y_train.values)
# 테스트 데이터 정확도
model.score(x_test.values, y_test.values)
# rent 2550
# 0, 1, 400, 9, 2, 17, 1, 1, 9, 9, 1, 1, 9, 1
my_apt = [[0, 1, 400, 9, 2, 17, 1, 1, 9, 9, 1, 1, 9, 1]]
pred = model.predict(my_apt)
print('우리집 예측값 : ', pred)

y_hat = model.predict(x_test.values)
plt.scatter(y_test.values, y_hat, alpha=0.4)
plt.xlabel('actual rent')
plt.xlabel('predicted rent')
plt.title('rent')
plt.show()

plt.scatter(df[['size_sqft']], df[['rent']], alpha=0.4)
plt.show()
plt.scatter(df[['building_age_yrs']], df[['rent']], alpha=0.4)
plt.show()
