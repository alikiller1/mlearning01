#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 18:19
# @Author  : liuqh
# @Software: PyCharm

from utils import timeit
import time

from loggingTest import logger

class c1:
    def __init__(self,city='上海'):
        self.city=city

    # @timeit
    def f1(self,country, **kwargs):
        time.sleep(1)
        logger.info('I am %d years old!' % kwargs['age'])

    @timeit
    def f2(self):
        time.sleep(1)
        logger.info('123')
        return self.city


if __name__ == '__main__':
    params:{
        'name':'liu',
        'age':10
    }
    c1=c1('北京');
    c1.f1('中国',**{'age':20})
    c1.f2()
