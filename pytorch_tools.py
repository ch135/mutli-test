# -*- coding: utf-8 -*-
"""
@project: mutli-test
@author: chenhao
@file: pytorch_tools.py
@ide: PyCharm
@time: 2019/7/11 0011 17:45
@todo: pytorch 实用工具集合
"""
import torch
import torchvision

import torch.nn as nn
from torch.autograd import Variable
import torchvision.models as models

import numpy as  np


# 参数输出测试
def test():
    model = models.resnet18()
    print("====================")
    for name, parameters in model.named_parameters():
        print(name, ":", parameters)

    print("=====================")
    print(model.layer1[0].conv1.weight.data)
    print(model.layer1[0].conv1.__class__)

    print("=======================")
    input = Variable(torch.randn(20, 16, 50, 100))
    print(input.size())
    print(np.prod(input.size()))


# 模型参数数目统计
def parm_nums():
    model = models.vgg19()
    total = sum([param.nelement() for param in model.parameters()])
    print("Number of params: %.2fM" % (total / 1e6))

#

if __name__ == "__main__":
    parm_nums()
