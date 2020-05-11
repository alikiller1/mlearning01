#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 16:34
# @Author  : liuqh
# @Software: PyCharm
import time
from loggingTest import logger

def timeit(f):
    def wrapper(*args, **kwargs):		#*args：接收多个参数；**kwargs：关键字传参，接收多个参数
        start_time = time.time()		#函数开始运行时间
        res = f(*args, **kwargs)
        if 'age' in kwargs:
            logger.info('ddd-123')
        end_time = time.time()		    #函数结束时间
        logger.info("%s函数运行时间为：%.8f" %(f.__name__, end_time - start_time))
        logger.info(f'{f.__name__} 返回结果 {res}')
        return res			#返回函数运行时间
    return wrapper
