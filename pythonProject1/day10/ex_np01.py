import numpy as np
list1 = [1, 2, 3, 4]
print('list1 : ', list1)
print('list1 type : ', type(list1))

array1 = np.array(list1)
print('array1 : ', array1)
print('array1 type : ', type(array1))

print('array1 데이터 타입 : ', array1.dtype)
print('구조 : ', array1.shape)
print('1차원 : ', array1.ndim)

# arr2 = np.array([list1, [4, 5, 6, 7]])
arr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
print('2차원 : ', arr2.ndim, arr2.shape, arr2.dtype)
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[3, 2, 1], [4, 5, 6]]])
print('3차원 : ', arr3.ndim, arr3.shape, arr3.dtype)
arr4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[3, 2, 1], [4, 5, 6]]]
                , [[[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]])
print('4차원 : ', arr4.ndim, arr4.shape, arr4.dtype)

# numpy는 벡터 연산을 지원
a = np.array([[1, 2]
             , [3, 4]])
b = np.array([[0, 1]
             , [2, 3]])
c = np.dot(a, b)  # dot product
print('dot product : ', c)
print('T', np.transpose(c))  # 전치행렬

# 쉐잎 바꾸기 가능
test_arr = np.arange(10)  # 0 ~ 9
print('='*100)
print(test_arr)
print('2 x 5\n', test_arr.reshape(2, 5))
print('5 x 2\n', test_arr.reshape(5, 2))

