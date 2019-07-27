# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/24 11:07
@month : 六月
@Author : mhm
@FileName: 1、求开方.py
@Software: PyCharm
'''
'''
Input: 4
Output: 2
一个数 x 的开方 sqrt 一定在 0 ~ x 之间，并且满足 sqrt == x / sqrt。
可以利用二分查找在 0 ~ x 之间查找 sqrt。

对于 x = 8，它的开方是 2.82842...，最后应该返回 2 而不是 3。
在循环条件为 l <= h 并且循环退出时，h 总是比 l 小 1，
也就是说 h = 2，l = 3，因此最后的返回值应该为 h 而不是 l。
'''
# 二分查找
def mySqrt(x):
    if x == 1:
        return 1
    l = 1
    h = x/2
    while h > l:
        m = (l+h)//2
        if m**2 > x:
            h = m-1
        elif m**2 < x:
            l = m+1
        else:
            return m
    if h == l:
        if (h-1)**2 < x < h**2:
            return h-1
        else:
            return h
    elif h < l:
        return h

print(mySqrt(9))






