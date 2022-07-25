# 평균제곱오차 MSE(MEAN SQUARED ERROR)
import numpy as np
import matplotlib.pyplot as plt

# x1 : 공부 시간, x2 : 과외 시간, y : 점수
data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
x1 = [i[0] for i in data]  # 공부 시간
x2 = [i[1] for i in data]  # 과외 시간
y = [i[2] for i in data]   # 점수

ax = plt.axes(projection='3d')
ax.set_xlabel('study hours')
ax.set_ylabel('private class')
ax.set_zlabel('score')
ax.dist = 11
ax.scatter(x1, x2, y)
plt.show()

x1_data = np.array(x1)
x2_data = np.array(x2)
y_data = np.array(y)

a1 = 0
a2 = 0
b = 0
lr = 0.05
epochs = 2001
# 검사 하강법 GD
for i in range(epochs):
    y_hat = a1 * x1_data + a2 * x2_data + b
    error = y_data - y_hat  # 오차
    a1_diff = -(1/len(x1_data)) * sum(x1_data * error) # 오차 함수를 a로 미분
    a2_diff = -(1/len(x2_data)) * sum(x2_data * error) # 오차 함수를 a로 미분
    b_diff = -(1/len(x1_data)) * sum(y_data - y_hat)   # 오차 함수를 b로 미분

    a1 = a1 - lr * a1_diff  # 학습 률을 곱해 기존의 a2값 업데이트
    a2 = a2 - lr * a2_diff  # 학습 률을 곱해 기존의 a1값 업데이트
    b = b - lr * b_diff     # 학습 률을 곱해 기존의 a값 업데이트
    if i % 100 == 0:
        print('epoch : %.f, 기울기1 : %.04f, 기울기2 : %.04f, 절편 : %0.04f' % (i, a1, a2, b))
        print('오차 : ', error)
# pip install statsmodels
# 다중 선형 회귀 '예측 평면' 3D
import statsmodels.api as statm
import statsmodels.formula.api as statfa
import pandas as pd
x = [i[0:2] for i in data]
y = [i[2] for i in data]
x_1 = statm.add_constant(x)
results = statm.OLS(y, x_1).fit()
hour_class = pd.DataFrame(x, columns=['study_hours', 'private_class'])
hour_class['score'] = pd.Series(y)
model = statfa.ols(formula='score ~ study_hours + private_class', data=hour_class)
result_formula = model.fit()
a, b = np.meshgrid(np.linspace(hour_class.study_hours.min(), hour_class.study_hours.max(), 100)
                   , np.linspace(hour_class.private_class.min(), hour_class.private_class.max(), 100))
x_ax = pd.DataFrame({'study_hours':a.ravel(), 'private_class':b.ravel()})
fittedy = result_formula.predict(exog=x_ax)
fig = plt.figure()
graph = fig.add_subplot(111, projection='3d')
graph.scatter(hour_class['study_hours'], hour_class['private_class'], hour_class['score'], c='blue', marker='o', alpha=1)
graph.plot_surface(a, b, fittedy.values.reshape(a.shape)
                   , rstride=1, cstride=1, color='none', alpha=0.4)
graph.set_xlabel('study_hours')
graph.set_ylabel('private_class')
graph.set_zlabel('score')
graph.dist = 11
plt.show()






