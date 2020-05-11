#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 22:33
# @Author  : liuqh
# @Software: PyCharm

import numpy as np

x=np.random.uniform(-3,3,size=100)
print(x)
print(type(x))
print('----------------')
b=np.random.normal(0,1,size=100)
print(b)

for letter in 'Python':
   if letter == 'h':
      pass
      print ('这是 pass 块')
   else: print ('当前字母 :', letter)

print ('Good bye!')

a=[1,2,3]

b=[2,3,4]
a=np.mat(a).T
b=np.mat(b).T
c=np.hstack([a,b]);
print(c)

a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
a=np.mat(a);
print(a.shape)
print(a[:2,2:])

a=np.arange(1,11);
print(type(a))
print(a.shape)
a=a.reshape(-1,2)
print(a.shape)

print(np.matrix(a))