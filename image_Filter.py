# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 22:18
# @Author  : chenhao
# @FileName: image_Filter.py
# @Software: PyCharm
# @Desc: 图像不同卷积核处理比较
'''
    结论：
    1）不同大小的滤波器，会丢失不同的图像信息；滤波器越大，丢失信息越多
    2）直接将不同卷积核生成的图像相加起来时，会使像素值大于255，造成图像斑块。这可以通过深度学习不同迭代训练进行解决
    问题：
    神经网络的构建怎么构建好？？？
    1）使用残差网络直接相加
    2）使用DenseNet相叠加，再进行揉合
    3）使用MixNet相叠加，再进行揉合
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import compare_psnr as psnr, compare_ssim as ssim

img = cv2.imread("3.jpg")[..., ::-1]
kernel1 = np.ones((3, 3), np.float32) / 9
kernel2 = np.ones((5, 5), np.float32) / 9
kernel3 = np.ones((7, 7), np.float32) / 9

img1 = cv2.filter2D(img, kernel=kernel1, ddepth=-1, dst=-1)
img2 = cv2.filter2D(img, kernel=kernel2, ddepth=-1, dst=-1)
img3 = cv2.filter2D(img, kernel=kernel3, ddepth=-1, dst=-1)
img4 = img1 + img2 + img3

psnr1 = psnr(img, img1)
psnr2 = psnr(img, img2)
psnr3 = psnr(img, img3)
psnr4 = psnr(img, img4)
ssim1 = ssim(img, img1, multichannel=True)
ssim2 = ssim(img, img2, multichannel=True)
ssim3 = ssim(img, img3, multichannel=True)
ssim4 = ssim(img, img4, multichannel=True)

plt.subplot(2, 3, 1), plt.imshow(img), plt.title('source')
plt.subplot(2, 3, 2), plt.imshow(img1), plt.title('k3/{:.2f}/{:.2f}'.format(psnr1, ssim1))
plt.subplot(2, 3, 3), plt.imshow(img2), plt.title('k5/{:.2f}/{:.2f}'.format(psnr2, ssim2))
plt.subplot(2, 3, 4), plt.imshow(img3), plt.title('k7/{:.2f}/{:.2f}'.format(psnr3, ssim3))
plt.subplot(2, 3, 5), plt.imshow(img4), plt.title('multi/{:.2f}/{:.2f}'.format(psnr4, ssim4))

plt.savefig('multi-filter.jpg')
plt.show()
