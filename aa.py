#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 16:35
# @Author  : liuqh
# @Software: PyCharm

import getpass
import time


# 获取username, 如chinaren
def getusername():
    username = getpass.getuser() # 获取当前用户名
    # 获取当前的username
    return username

# 获取时间和日期
def getnowdatatime(flag=0):
    '''
    flag = 0为时间和日期         eg:2018-04-11 10:04:55
    flag = 1仅获取日期           eg:2018-04-11
    flag = 2仅获取时间           eg:10:04:55
    flag = 3纯数字的日期和时间   eg:20180411100455
    '''
    now = time.localtime(time.time())
    if flag == 0:
        return time.strftime('%Y-%m-%d %H:%M:%S', now)
    if flag == 1:
        return time.strftime('%Y-%m-%d', now)
    if flag == 2:
        return time.strftime('%H:%M:%S', now)
    if flag == 3:
        return time.strftime('%Y%m%d%H%M%S', now)


# 生成指定大小的TXT档
def generateTXTFile():
    fileSize = 0
    # 判断输入是否有误
    while True:
        size = input('请输入你想生成的TXT文件大小(MB):')
        if size.strip().isdigit() != True:
            print('只能输入整数，请重新输入!')
            continue
        else:
            fileSize = int(size)
            break
    if fileSize >= 200:
        print('正在生成TXT文件，请稍候... ...')
    # 生成指定大小的TXT档
    filename = getnowdatatime(3) + '_' + size + 'MB.txt'
    print(f'文件名：{filename}')
    # 设置文件保存的路径
    filepath = './'
    print(filepath+filename)

    f = open(filepath+filename, 'a')
    # 获取开始时间
    starttime = getnowdatatime()

    for i in range(fileSize):
        if i >= 100:
            if i % 100 == 0:
                print(f'已生成{i // 100 * 100}MB数据.')
        for j in range(1024):
            try:
                f.write('你好中国')
            except KeyboardInterrupt:
                print('\n异常中断:KeyboardInterrupt')
                f.close()
                exit(-1)
    f.close()
    print(f'文件已成生并保存在桌面,  文件大小:{fileSize}MB.\n')

    print('01' *2)


if __name__ == '__main__':
    generateTXTFile()
