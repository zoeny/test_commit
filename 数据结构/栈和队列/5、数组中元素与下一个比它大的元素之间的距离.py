# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/28 10:46
@month : 六月
@Author : mhm
@FileName: 5、数组中元素与下一个比它大的元素之间的距离.py
@Software: PyCharm
'''
'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输入
是你需要再等待多久温度才会升高的天数。如果之后都不会升高，请输入 0 来代替。

在遍历数组时用栈把数组中的数存起来，如果当前遍历的数比栈顶元素来的大，
说明栈顶元素的下一个比它大的数就是当前元素。

给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
'''
def dailyTemperatures(T):
    res = [0]*len(T)
    s = []
    for i in range(0,len(T)):
        while s and T[i] > T[s[-1]]:
            res[s[-1]] = i-s[-1]
            s.pop()
        s.append(i)
    return res

# 方法二
def dailyTemp(T):
    l = len(T)
    a = [0]*l
    for i in range(l):
        p = 0
        for j in range(i,l):
            if T[j]>T[i]:
                p = j-i
                a[i] = p
                break
    return a
















