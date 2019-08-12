# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 14:04
# @Author  : chenhao
# @FileName: loggingText.py
# @Software: PyCharm
# @Desc: logging 测试
import logging
import log_util as log
import time

'''
1. 日志一共分成5个等级，低到高：DEBUG INFO WARNING ERROR CRITICAL
2. 日志格式说明
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息
'''


# 日志存入到 txt 文件中
def toFile():
    logging.basicConfig(level=logging.DEBUG, filename='./log/log.txt', filemode='a',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


# 日志输出到控制台和日志文件中
def toFileAndContro():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 输出到不同平台的总开关

    file = logging.FileHandler('./log/logfile.txt', mode='a')  # 日志输出到文件的设置
    file.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()  # 日志输出到控制台的设置
    ch.setLevel(logging.WARNING)

    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # 日志输出格式设置
    file.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 将不同控制模块添加到总控制台
    logger.addHandler(file)
    logger.addHandler(ch)


if __name__ == '__main__':
    toFileAndContro()

    logging.debug('the message of debug')
    logging.info("the message of info")
    log.fun()   # 模块的责行顺序就是日志的输出顺序
    logging.warning('the message of warning')
    logging.error('the message of error')
    logging.critical('the message of critical')
    logging.critical(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))
