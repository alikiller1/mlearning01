#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/23 20:09
# @Author  : liuqh
# @Software: PyCharm

import jieba
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == "__main__":
    corpus = ["日本 法国",
               "南京 长沙 深圳"]
    corpus2 = ["中国 美国",
                "北京 上海"]
    transformer = TfidfVectorizer()
    transformer.fit(corpus2)    # 该类会统计每个词语的tf-idf权值
    print("-----------------")
    transformer.fit(corpus)

    c=transformer.transform(corpus)

    print(c.toarray())