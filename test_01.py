#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 22:22
# @Author  : liuqh
# @Software: PyCharm

from p2 import a_model;
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-a','--age', dest="age", type=int, required=True,
                        help='display an integer')
    parser.add_argument("-v", "--verbose",dest='vv', help="increase output verbosity",
                    action="store_true")
    args = parser.parse_args()
    i=0;
    while i <len(sys.argv):
        print(sys.argv[i])
        i=i+1
    if args.vv:
        print ("verbosity turned on")
    print(args.age)
