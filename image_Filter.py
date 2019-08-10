# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 22:18
# @Author  : chenhao
# @FileName: image_Filter.py
# @Software: PyCharm
# @Desc: 图像不同卷积核处理比较
'''
    结论：不同大小的滤波器，会丢失不同的图像信息；滤波器越大，丢失信息越多
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("3.jpg")
kernel1 = np.ones((3, 3), np.float32) / 9
kernel2 = np.ones((5, 5), np.float32) / 9
kernel3 = np.ones((7, 7), np.float32) / 9

img1 = cv2.filter2D(img, kernel=kernel1, ddepth=-1, dst=-1)
img2 = cv2.filter2D(img, kernel=kernel2, ddepth=-1, dst=-1)
img3 = cv2.filter2D(img, kernel=kernel3, ddepth=-1, dst=-1)

plt.subplot(2, 2, 1), plt.imshow(img), plt.title('source')
plt.subplot(2, 2, 2), plt.imshow(img1), plt.title('f3')
plt.subplot(2, 2, 3), plt.imshow(img2), plt.title('f5')
plt.subplot(2, 2, 4), plt.imshow(img3), plt.title('f7')

plt.savefig('multi-filter.jpg')
plt.show()

