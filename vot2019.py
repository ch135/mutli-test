# -*- coding: utf-8 -*-
"""
@project: myTest
@author: chenhao
@file: vot2019.py
@ide: PyCharm
@time: 2019/7/8 0008 16:17
@todo: 解压缩文件
"""
import zipfile
import os


def un_zip(path, fileanme):
    zip = zipfile.ZipFile(fileanme)
    for name in zip.namelist():
        zip.extract(name, path)


for root, dirs, _ in os.walk("./"):
    for dir in dirs:
        path = os.path.join(root, dir)

        zip_files = os.listdir(path)
        for zip_file in zip_files:
            filename = os.path.join(path, zip_file)
            un_zip(path, filename)
