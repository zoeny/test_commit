# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/18 12:44
@month : 六月
@Author : mhm
@FileName: 2、两数平方和.py
@Software: PyCharm
'''

# 题目描述：判断一个数是否为两个数的平方和。是返回True，反之，返回False
def is_TwoSum(target):
    import math
    i,j = 0,math.sqrt(target)
    while i < j:
        c = i * i + j * j
        if target == c:
            return True
        elif target > c:
            i += 1
        else:
            return False
print(is_TwoSum(16))

























