# -*- coding: utf-8 -*-
"""
@project: mutli-test
@author: chenhao
@file: image_FFT.py
@ide: PyCharm
@time: 2019/7/29 0029 17:37
@todo: 图像的傅里叶变化
"""
import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread("E:/haochen/qq.jpg", 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

s1 = np.log(np.abs(f))
s2 = np.log(np.abs(fshift))

img_back = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(img_back)
img_back = np.abs(img_back)

plt.subplot(221), plt.imshow(s1, 'gray'), plt.title('original')
plt.subplot(222), plt.imshow(s2, 'gray'), plt.title('center')
plt.subplot(223), plt.imshow(img, 'gray'), plt.title('source')
plt.subplot(224), plt.imshow(img_back, 'gray'), plt.title('img_back')

plt.show()
