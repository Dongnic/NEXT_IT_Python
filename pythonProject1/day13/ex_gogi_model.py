from keras.preprocessing.image import ImageDataGenerator
from keras import models, layers, optimizers
from keras.layers import Flatten, Dropout, Dense
from keras.applications import VGG16
import keras.backend as K
from keras.models import load_model
from keras.utils.image_utils import load_img, img_to_array
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 이미지 생성
train_dir = './split_dataset/train'
test_dir = './split_dataset/test'
# 학습 테스트 이미지 경로
save_model = './model/다람쥐.h5'
batch_size = 32
image_size = 224

train_datagen = ImageDataGenerator(
    rotation_range=180,  # 회전 최대 180
    width_shift_range=0.2,  # 좌우 이동
    height_shift_range=0.2,  # 상하 이동
    horizontal_flip=True,  # 좌우 반전
    vertical_flip=True  # 상하 반전
)
test_datagen = ImageDataGenerator()
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(image_size, image_size),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True
)
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(image_size, image_size),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True
)
class_num = len(train_generator.class_indices)
print('class 수 : ', class_num)
labels = list(test_generator.class_indices.keys())
print('학습 class 명 : ', labels)

K.clear_session()
conv_layer = VGG16(weights='imagenet', include_top=False, input_shape=(image_size, image_size, 3))
conv_layer.summary()

# 학습이 되어서 가져온 가중치는 학습되지 않게 설정
for layer in conv_layer.layers:
    layer.trainable = False

model = models.Sequential()
model.add(conv_layer)
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(class_num, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(learning_rate=1e-4)
              , metrics=['acc'])
history = model.fit(train_generator
                              , steps_per_epoch=train_generator.samples/train_generator.batch_size
                              , epochs=100
                              , validation_data=test_generator
                              , validation_steps=test_generator.samples/test_generator.batch_size
                              , verbose=1)
model.save(save_model)
import matplotlib.pyplot as plt

acc = history.history['acc']
loss = history.history['loss']
cnt = range(len(acc))
plt.plot(cnt, acc, 'b', label='acc')
plt.plot(cnt, loss, 'r', label='loss')
plt.title('acc and loss')
plt.legend()
plt.show()