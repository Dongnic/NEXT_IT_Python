# 평균제곱오차 MSE(MEAN SQUARED ERROR)
import numpy as np
import matplotlib.pyplot as plt
# pip install sklearn
from sklearn.linear_model import LinearRegression

# 가상의 a(기울기)와 b(y절편)
a_b = [3, 76]
# x:공부시간 y:점수
data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# list to ndarray
x_data = np.array(x)
y_data = np.array(y)
# 초기값 hyper param 직접 지정하는 변수
model = LinearRegression()
model.fit(x_data.reshape(-1, 1), y_data)
print(model.coef_)          # 기울기
print(model.intercept_)     # y절편
print(model.predict([[5]])) # 5시간 학습 했을 때

plt.plot(x_data.reshape(-1, 1), y_data, 'o')
plt.plot(x_data.reshape(-1, 1), model.predict(x_data.reshape(-1, 1)))
plt.show()