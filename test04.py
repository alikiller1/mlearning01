#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/11 11:58
# @Author  : liuqh
# @Software: PyCharm
from utils import logger


def f1(a,b):
    """
    求和方法
    :param a:float a
    :param b:float a
    :return:a+b
    """
    sum=a+b;
    logger.info("sum=%d" %sum)
    return sum

if __name__ == '__main__':
    a = 2;
    b = 2;
    if (not a == 1) and b == 2:
        logger.info(3)
    else:
        print(4)
    f1(1,2)
