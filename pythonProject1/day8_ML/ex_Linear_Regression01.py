# 평균제곱오차 MSE(MEAN SQUARED ERROR)
import numpy as np
import matplotlib.pyplot as plt

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
a = 0
b = 0
lr = 0.05       # 학습률
epochs = 2001   # 학습 횟수
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
        print('오차 : ', error)
y_pred = a * x_data + b
plt.scatter(x, y)
plt.plot([min(x_data), max(x_data)], [min(y_pred), max(y_pred)])
plt.show()
