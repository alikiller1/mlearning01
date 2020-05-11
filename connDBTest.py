#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 9:54
# @Author  : liuqh
# @Software: PyCharm


from sqlalchemy import create_engine
from string import Template


engine = create_engine('mysql://root:123@localhost:3306/testdb?charset=utf8mb4')
#engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/testdb?charset=utf8mb4');
#engine = create_engine('postgresql+pg8000://postgres:123@localhost:5432/testdb')

result = engine.execute('SELECT * FROM USER')

print(result.fetchall())
