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

# 计算模型运算量
def model_flops():

    prods = {}
    def save_hook(name):
        def hook_per(self, input, output):
            prods[name] = np.prod(input[0].shape)
        return hook_per

    list_1 = []
    def simple_hook(self, input, output):
        list_1.append(np.prod(input[0].shape))

    list_2 = {}
    def simple_hook2(self, input, output):
        list_2["names"] = np.prod(input[0].shape)

    """
    卷积核运算次数的计算
    flop = output_batch * output_weight * output_height * output_channel * params
    因此，主要求出 params 的个数。params 主要包含卷积核+偏置值的数目
    kernel = kernel_width * kernel_height * (in_channel/groups_num)*(2 if multiply_adds else 1)
    """
    multiply_adds = False
    list_conv = []

    def conv_hook(self, input, output):
        batch_size, input_channels, input_height, input_width = input[0].size()
        output_channels, output_height, output_width = output[0].size()

        kernel_ops = self.kernel_size[0] * self.kernel_size[1] * (self.in_channels / self.groups) * (
            2 if multiply_adds else 1)
        bias_ops = 1 if self.bias is not None else 0

        params = output_channels * (kernel_ops + bias_ops)
        flops = batch_size * params * output_height * output_width

        list_conv.append(flops)

    """
    全连接层计算量
    flop = batch_size * (weight_num + bias_num)
    
    batch_size 与输入向量的维度有关。当输入为[a]时， batch_size = 1；当输入为[[a]]时，batch_size = input.shape[0]
    weight_num：当输入为(1, a)，输出为(1, b)时，weight_num = a * b
    bias_num = 0 或 b
    """
    list_linear = []

    def linear_hook(self, input, output):
        batch_size = input[0].size(0) if input[0].dim() == 2 else 1

        weight_ops = self.weight.nelement() * (2 if multiply_adds else 1)
        bias_ops = self.bias.nelement()

        flops = batch_size * (weight_ops + bias_ops)
        list_linear.append(flops)

    """
    归一化计算量：
    Y = y(x-u)/(o+b)
    可得 计算量为 x 的个数
    """
    list_bn=[]

    def bn_hook(self, input, output):
        list_bn.append(input[0].nelement())

    list_relu=[]

    def relu_hook(self, input, output):
        list_relu.append(input[0].nelement())

    """
    池化层计算量和 卷积层计算量相似，只是池化层没对特征层分组和相加，也没有偏置值 b
    """
    list_pooling = []

    def pooling_hook(self, input, output):
        batch_size, input_channels, input_height, input_width = input[0].size()
        output_channels, output_height, output_width = output[0].size()

        kernel_ops = self.kernel_size * self.kernel_size
        bias_ops = 0
        params = output_channels * (kernel_ops + bias_ops)
        flops = batch_size * params * output_height * output_width

        list_pooling.append(flops)

    def foo(net):
        childrens = list(net.children())
        if not childrens:
            if isinstance(net, torch.nn.Conv2d):
                # net.register_forward_hook(save_hook(net.__class__.__name__))
                # net.register_forward_hook(simple_hook)
                # net.register_forward_hook(simple_hook2)
                net.register_forward_hook(conv_hook)
            if isinstance(net, torch.nn.Linear):
                net.register_forward_hook(linear_hook)
            if isinstance(net, torch.nn.BatchNorm2d):
                net.register_forward_hook(bn_hook)
            if isinstance(net, torch.nn.ReLU):
                net.register_forward_hook(relu_hook)
            if isinstance(net, torch.nn.MaxPool2d) or isinstance(net, torch.nn.AvgPool2d):
                net.register_forward_hook(pooling_hook)
            return
        for c in childrens:
            foo(c)

    resnet = models.alexnet()
    foo(resnet)
    input = Variable(torch.rand(3, 224, 224).unsqueeze(0), requires_grad=True)
    out = resnet(input)

    total_flops = (sum(list_conv) + sum(list_linear) + sum(list_bn) + sum(list_relu) + sum(list_pooling))

    print('  + Number of FLOPs: %.2fG' % (total_flops / 1e9))

# 输出前向传播的结果
def print_forward():
    model = torchvision.models.resnet18()
    select_layer = model.layer1[0].conv1

    grads = {}
    def save_grad(name):
        def hook(self,input, output):
            grads[name] = input
        return hook

    select_layer.register_forward_hook(save_grad("select_layer"))

    input = Variable(torch.rand(3, 244, 244).unsqueeze(0), requires_grad = True)

    out = model(input)
    print(grads)

if __name__ == "__main__":
    print_forward()
