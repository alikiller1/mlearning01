#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 22:26
# @Author  : liuqh
# @Software: PyCharm

import traceback

a = 1
a = None
a = [1, 2, 3]

file_object = open('./aaa.csv', 'w')
for i in a:
    file_object.write(str(i) + '\n')
file_object.close()

file_object = open('./aaa.csv', 'r')
try:
    line = file_object.readline()
    print(d)
    while line:
        print('line->%s' % line)
        line = file_object.readline()
except Exception as e:
     traceback.print_exc()
finally:
    file_object.close()

