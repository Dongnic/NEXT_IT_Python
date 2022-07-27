import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier

x = [[0, 0]
     , [1, 0]
     , [0, 1]
     , [1, 1]]
# y = [0, 0, 0, 1]  # and
# y = [0, 1, 1, 1]  # or
y = [0, 1, 1, 0]  # xor perceptron 하나 로는 못 맞춤

model = Perceptron(tol=1e-3, random_state=0)
model.fit(x, y)
print(model.predict(x))

# xor  맞춤
multi_model = MLPClassifier(tol=1e-3, random_state=0, max_iter=1000)
multi_model.fit(x, y)
print(multi_model.predict(x))