# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 20:02
@month : 六月
@Author : mhm
@FileName: 3、最小值栈.py
@Software: PyCharm
'''

# 方法1：时间复杂度O(n)
class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)

# 方法2：时间复杂度O(1)
class MinStack1(object):
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self,x):
        if self.stack_min == [] or self.stack_min[-1]>=x:
            self.stack_min.append(x)
        self.stack.append(x)

    def pop(self):
        if self.stack_min[-1] == self.stack[-1]:
            self.stack_min.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stack_min[-1]







