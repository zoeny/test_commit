# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/29 15:14
@month : 六月
@Author : mhm
@FileName: 5、母牛生产.py
@Software: PyCharm
'''
'''
题目描述：假设农场中成熟的母牛每年都会生 1 头小母牛，并且永远不会死。第一年有 1 只小母牛，从第二年开始，母牛开始生小母牛。每只小母牛 3 年之后成熟又可以生小母牛。
给定整数 N，求 N 年后牛的数量。
第 i 年成熟的牛的数量为：
dp[i]=dp[i-1]+dp[i-3]
'''
def cowCount(n):
    cow = [0]*(n)
    cow[0] = 1
    cow[1] = 2
    cow[2] = 3
    for i in range(3,n):
        cow[i] = cow[i-1]+cow[i-3]
    return cow[-1]
print(cowCount(6))



















