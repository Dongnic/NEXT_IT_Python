# 평균제곱오차 MSE(MEAN SQUARED ERROR)
import numpy as np
import matplotlib.pyplot as plt

# 가상의 a(기울기)와 b(y절편)
a_b = [3, 76]
# x:공부시간 y:점수
data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# 그래프
plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()


# MSE함수
def mse(y, y_hat):
    return ((y - y_hat) ** 2).mean()


def mse_val(y, predict_result):
    return mse(np.array(y), np.array(predict_result))


# 예측 값
predict_result = []


# 예측함수
def predict(x):
    return a_b[0] * x + a_b[1]


# x값에 대입
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print('공부시간 : %.f, 실제점수 : %.f 예측점수 : %.f' % (x[i], y[i], predict(x[i])))
# 최종 MSE
print('MSE 최종 값 : ', mse_val(predict_result, y))
