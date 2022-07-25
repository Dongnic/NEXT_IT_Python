# 평균제곱오차 MSE(MEAN SQUARED ERROR)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv('./datasets/heights.csv')
print(df.head())

# x:공부시간 y:점수
x = df['height']
y = df['weight']
plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

# list to ndarray
x_data = np.array(x.round())
y_data = np.array(y.round())
# 초기값 hyper param 직접 지정하는 변수
a = 0.1
b = 0.1
lr = 0.0001       # 학습률
epochs = 20001   # 학습 횟수
error = 0
# 검사 하강법 GD
for i in range(epochs):
    y_hat = a * x_data + b
    error = y_data - y_hat  # 오차
    a_diff = -(1/len(x_data)) * sum(x_data * error) # 오차 함수를 a로 미분
    b_diff = -(1/len(x_data)) * sum(error)          # 오차 함수를 b로 미분

    a = a - lr * a_diff # 학습률을 곱해 기존의 a값 업데이트
    b = b - lr * b_diff # 학습률을 곱해 기존의 a값 업데이트
    if i % 100 == 0:
        print('epoch : %.f, 기울기 : %.04f, 절편 : %0.04f' % (i, a, b))
y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()

