# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 20:47
# @Author  : chenhao
# @FileName: getXmlVal.py
# @Software: PyCharm
# @Desc: python 读取 xml 文件数据
import os
import xml.dom.minidom as xmldom

root = "./data"
files = [file for file in os.listdir(root) if os.path.splitext(file)[1] == ".xml"]

for file in files:
    path = os.path.join(root, file)
    result = os.path.join(root, "result.txt")
    dom = xmldom.parse(path)
    # 获取某个节点数据
    # width height 代表图像大小
    width = dom.getElementsByTagName("width")[0].firstChild.data
    height = dom.getElementsByTagName("height")[0].firstChild.data
    xmin = dom.getElementsByTagName("xmin")[0].firstChild.data
    ymin = dom.getElementsByTagName("ymin")[0].firstChild.data
    xmax = dom.getElementsByTagName("xmax")[0].firstChild.data
    ymax = dom.getElementsByTagName("ymax")[0].firstChild.data

    with open(result, "a") as f:
        f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (width, height, xmin, ymin, xmax, ymax))
