# pip install keras
# pip install tensorflow
# 만약에 CPU만 사용한다면
# pip install tensorflow-cpu

import sys

from keras.datasets import mnist
from keras.utils import np_utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 코드로 확인
for x in x_train[5]:
    for i in x:
        sys.stdout.write('%d\t' % i)
    sys.stdout.write('\n')
print('class : %d' % y_train[5])

# 그래프로 확인
import matplotlib.pyplot as plt
plt.imshow(x_train[5], cmap='Reds')
plt.show()
