from keras.models import load_model
model = load_model('./model/vgg16_dental.h5')
print(model.summary())
from keras.utils.image_utils import load_img, img_to_array
import numpy as np


def fn_test(p_model, filepath):
    image = load_img(filepath, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, 224, 224, 3))
    yhat = p_model.predict(image)
    idx = np.argmax(yhat[0])
    print(idx)


files = ['../day12/dental_image/test/healthy/1.jpg'
         , '../day12/dental_image/test/cured/301.jpg'
         , '../day12/dental_image/test/decayed/101.jpg']
for file in files:
    fn_test(model, file)