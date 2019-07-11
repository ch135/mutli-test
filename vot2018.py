# -*- coding: utf-8 -*-
"""
@project: myTest
@author: chenhao
@file: vot2018.py
@ide: PyCharm
@time: 2019/7/5 0005 21:21
@todo: 在 子文件中创建文件夹
"""
import os
import shutil

for root, dirs, _ in os.walk("./"):
    for dir in dirs:
        path = "{0}{1}/{2}".format(root, dir, "color")
        if not os.path.exists(path):
            os.makedirs(path)

        files = os.listdir(os.path.join(root, dir))
        for file in files:
            fpath = "{0}{1}/{2}".format(root, dir, file)
            shutil.move(fpath, path)

