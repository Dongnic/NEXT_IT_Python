import numpy as np

x = np.array([[0, 0]
             , [1, 0]
             , [0, 1]
             , [1, 1]])
# y = np.array([-1, -1, -1, 1]) # and 연산
y = np.array([-1, 1, 1, 1]) # or 연산
# y = np.array([-1, 1, 1, -1]) # xor 연산

w = np.array([1., 1., 1.])  # w1, w2, b


def feed_forward(param):
    return np.dot(param, w[1:]) + w[0]


def step_function(param):  # activation function으로 사용 (활성 함수)
    # 0보다 크면 1 아니면 -1을 리턴하는 함수
    return np.where(feed_forward(param) > 0, 1, -1)


print('before train', w)
lr = 0.01  # 학습률
for epoch in range(50):
    for x_val, y_val in zip(x, y):
        update = lr * (y_val - step_function(x_val))
        w[1:] += update * x_val
        w[0] += update
        print(w[0], w[1], w[2])
print('after train', w)
print('test')
for i, v in enumerate(x):
    print('input : ', v)
    print('output : ', step_function(v))





