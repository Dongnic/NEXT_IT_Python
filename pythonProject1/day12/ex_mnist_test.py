import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model = keras.models.load_model('./model/07-0.0263.hdf5')


def fn_read_list(path='./img/'):
    img_list = []
    file_list = os.listdir(path)
    for i in file_list:
        img_list.append(path + i)
    return img_list


def fn_img(imgPath):
    img = Image.open(imgPath).convert('L')  # 'L' <-- gray 컬러로 읽어옴
    img_resize = img.resize((28, 28))
    plt.imshow(img_resize)
    # plt.show()
    return np.array(img_resize).reshape(1, 28, 28, 1).astype('float32') / 255


test_list = fn_read_list()
for i in test_list:
    pred = model.predict(fn_img(i))
    print(np.argmax(pred, 1))
    print('1순위', np.argsort(np.max(pred, axis=0))[-1])
    print('2순위', np.argsort(np.max(pred, axis=0))[-2])
    print('3순위', np.argsort(np.max(pred, axis=0))[-3])
