import numpy as np
import matplotlib.pyplot as plt
# 공부한 시간: x 합격 여부: y
data = [[2, 0], [4, 0], [6, 0], [8, 1], [10, 1], [12, 1], [14, 1]]

x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

plt.scatter(x_data, y_data)
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)

# 기울기 a와 y절편 b의 값을 초기화
a = 0
b = 0
lr = 0.05  # 학습률
epochs = 2001


# 시그모이드 함수
def sigmoid(x):
    return 1 / (1 + np.e ** (-x))


# 검사 하강법 GD
for i in range(epochs):
    for x_data, y_data in data:
        a_diff = x_data * (sigmoid(a * x_data + b) - y_data)
        b_diff = sigmoid(a * x_data + b) - y_data
        a = a - lr * a_diff
        b = b - lr * b_diff
        if i % 100 == 0:
            print('epoch : %.f, 기울기 : %.04f, 절편 : %.04f' % (i, a, b))
x_range = np.arange(0, 15, 0.1)
plt.plot(x_range, np.array([sigmoid(a * x + b) for x in x_range]))
plt.show()