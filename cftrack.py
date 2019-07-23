# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 0:01
# @Author  : chenhao
# @FileName: cftrack.py
# @Software: PyCharm
# @Desc: 相关滤波目标追踪指标
import numpy as np
from numpy.fft import fft, fftshift
"""
:param response_map 每一帧响应的分数
"""
def APCE(response_map):
    Fmax = np.max(response_map)
    Fmin = np.min(response_map)
    apce = (Fmax - Fmin) ** 2 / (np.mean((response_map - Fmin) ** 2))
    return apce


"""
:parameter response 每一帧响应的分数
"""
def PSR(response):
    response_map = response.copy()
    # 获取矩阵中最大值得坐标
    max_loc = np.unravel_index(np.argmax(response_map, axis=None), response_map.shape)
    y, x = max_loc
    F_max = np.max(response_map)
    response_map[y - 5:y + 6, x - 5:x + 6] = 0.
    mean = np.mean(response_map[response_map > 0])
    # 计算矩阵标准差
    std = np.std(response_map[response_map > 0])
    psr = (F_max - mean) / std
    return psr

# 计算 AUC曲线的面积
def calAUC(value_list):
    length = len(value_list)
    delta = 1/(length-1)
    area = 0.0
    for i in range(1, length):
        area += delta*((value_list[i]+value_list[i-1])/2)
    return area


def cos_window(sz):
    """
    width, height = sz
    j = np.arange(0, width)
    i = np.arange(0, height)
    J, I = np.meshgrid(j, i)
    cos_window = np.sin(np.pi * J / width) * np.sin(np.pi * I / height)

    注：
    X, Y = np.meshgrid((0 1 2), (0 1))
    X = [[0 1 2], [0 1 2]]
    Y = [[0 0 0],[1 1 1]]
    """
    cos_window = np.hanning(int(sz[1]))[:, np.newaxis].dot(np.hanning(int(sz[0]))[np.newaxis, :])
    return cos_window
