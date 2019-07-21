#!/usr/bin/env python
# encoding: utf-8
# @project : myTest
# @author  : chenhao
# @file   : test.py
# @ide    : PyCharm
# @time   : 2019-06-20 17:26:16
# @desc:
import cv2
import os
import numpy as np


# ########### 摄像头测试 ##############
# video = cv2.VideoCapture(0)
# while True:
#     ret, frame = video.read()
#     cv2.imshow("test", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
## video.release()
# cv2.destoryAllwindows()

# ########### os测试 ##############
# print(__file__)
# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))

# ########### 数组测试 ##############
# text1 = [1, 2, 3, 4, 5]
# text2 = [1, 2, 3, 4, 5]
#
# print(np.mean(text1))

# ########### 文件写入测试 ##############
# with open("text.txt", "a") as file:
#     file.write("text")
#     file.write("\n")
#
# with open("text.txt", "a") as file:
#     file.write("text")
#     file.write("\n")

# ########### 图像合成视频测试 ##############
# def Video(path, size):
#     files = os.listdir(path)
#     fps = 25
#     v_path = "./basketball.mp4"
#     fourcc = cv2.VideoWriter_fourcc("D", "I", "V", "X")
#
#     video = cv2.VideoWriter(v_path, fourcc, fps, size)
#
#     for item in files:
#         if item.endswith(".jpg"):
#             item = path + "/" + item
#             img = cv2.imread(item)
#             video.write(img)
#
#     video.release()
#
#
# Video("E:/haochen/dataset/OTB100/basketball", (576, 432))

# # ########### 视频抽取图像测试 ##############
import os
import cv2


def videoToimg(video_path, img_path):
    videos = os.listdir(video_path)
    for video in videos:
        name, _ = video.split('.')
        vpath = os.path.join(video_path, video)
        impath = os.path.join(img_path, video.split('.')[0])

        if not os.path.exists(impath):
            os.makedirs(impath)

        cap = cv2.VideoCapture(vpath)
        frame_count = 1
        success = True
        while (success):
            success, frame = cap.read()

            params = []
            params.append(1)
            if (success):
                cv2.imwrite(impath + "/%d.jpg" % frame_count, frame, params)
            frame_count += 1
    cap.release()


if __name__ == '__main__':
    videoToimg("E:/haochen/dataset/track", "E:/haochen/dataset/track")
