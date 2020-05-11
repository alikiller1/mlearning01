#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 16:27
# @Author  : liuqh
# @Software: PyCharm
import sys

class a_model:
    @staticmethod
    def f1():
        print("f1 is  staticmethod")
am=a_model();

if __name__ == '__main__':
    am.f1();
    print(sys.path)