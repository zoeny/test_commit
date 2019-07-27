# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/26 9:02
@month : 六月
@Author : mhm
@FileName: 4、第一个错误的版本.py
@Software: PyCharm
'''
'''
题目描述：给定一个元素 n 代表有 [1, 2, ..., n] 版本，
在第 x 位置开始出现错误版本，导致后面的版本都错误。可以调用 isBadVersion(int x) 知道某个版本是否错误，要求找到第一个错误的版本
如果第 m 个版本出错，则表示第一个错误的版本在 [l, m] 之间，令 h = m；否则第一个错误的版本在 [m + 1, h] 之间，令 l = m + 1。
如果第 m 个版本出错，则表示第一个错误的版本在 [l, m] 之间，令 h = m；否则第一个错误的版本在 [m + 1, h] 之间，令 l = m + 1。
因为 h 的赋值表达式为 h = m，因此循环条件为 l < h。
'''
# 二分查找
def isBadVersion(n):
    return True

def firstBadVersion(n):
    l,h = 0,n
    while l<h:
        m = l + (h-l)//2
        if isBadVersion(m):
            h = m - 1
        else:
            l = m + 1
    return l

# 循环查找
def firstBadVersion1(n):
    for i in range(1,n):
        if not isBadVersion(i-1) and isBadVersion(i):
            return i+1