import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import keras.models
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
img = Image.open('./3.png').convert('L')  # 'L' <-- gray 컬러로 읽어옴
print(img.width, img.height)
plt.imshow(img)
plt.show()
re_img = img.resize((28, 28))
test_data = np.array(re_img).reshape(1, 784).astype('float32') / 255
print(test_data)
model = keras.models.load_model('./model/09-0.0599.hdf5')
pred = model.predict(test_data)
print(np.argmax(pred, 1))