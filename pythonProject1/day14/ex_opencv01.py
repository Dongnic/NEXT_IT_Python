# pip install opencv-python
# OpenCV 컴퓨터 비전 및 머신러닝 라이브러리 얼굴인식, 객체 식별, 이미지 결합 및 전처리
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('../day12/images/plane.jpg', cv2.IMREAD_COLOR)
# plt.imshow(image, cmap='gray')
plt.axis('off')
# plt.show()
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')
# 이미지 사이즈 조절
image_50 = cv2.resize(image, (50, 50))
plt.imshow(image_50)
# 이미지 블러처리
image_blur = cv2.blur(image, (100, 100))
plt.imshow(image_blur)
import numpy as np
kernel = np.array([[0, -1, 0]
                   , [-1, 5, -1]
                   , [0, -1, 0]])
# 선명하게 하는 필터(kernel)
conv = cv2.filter2D(image_rgb, -1, kernel)
plt.imshow(conv)
plt.axis('off')
plt.show()
