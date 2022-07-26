import numpy as np
import matplotlib.pyplot as plt


# 시그모이드 함수
def sigmoid(x):
    return 1 / (1 + np.e ** (-x))


# 랜덤 값 -8 ~ 8까지 사이 값 100개
x = np.linspace(-8, 8, 100)
sig = []
for i in x:
    sig.append(sigmoid(i))
plt.plot(x, sig)
plt.show()
