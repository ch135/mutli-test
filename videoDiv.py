# -*- coding: utf-8 -*-
"""
@project: myTest
@author: chenhao
@file: videoDiv.py
@ide: PyCharm
@time: 2019/7/3 0003 15:38
@todo:
"""
import cv2
import os
path = "./fmpeg"
if not os.path.exists(path):
    os.mkdir(path)
frame_count = 1
success = True
cap = cv2.VideoCapture("vtest.mov")
while(success):
    success, frame = cap.read()
    params = []
    params.append(1)
    cv2.imwrite(path + "/%d.ppm" % frame_count, frame, params)
    frame_count = frame_count+1

cap.release()