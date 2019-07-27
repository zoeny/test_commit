# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 18:10
@month : 六月
@Author : mhm
@FileName: 2、用队列实现栈.py
@Software: PyCharm
'''
'''
在将一个元素 x 插入队列时，为了维护原来的后进先出顺序，需要让 x 插入队列首部。而队列的默认插入顺序是队列尾部，因此在
将 x 插入队列尾部之后，需要让除了 x 之外的所有元素出队列，再入队列。
'''
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.pop() == []:
            return False
        else:
            return self.pop()

    def top(self):
        if self.stack == []:
            return False
        else:
            return self.stack[-1]
    def empty(self):
        if self.stack == []:
            return True
        else:
            return False

# 方法2：用两个队列实现栈
class MyStack1(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self,x):
        self.queue1.insert(0,x)

    def pop(self):
        for _ in range(len(self.queue1)):
            self.queue2.insert(0,self.queue1.pop())
        res = self.queue1.pop()
        self.queue1 = self.queue2
        self.queue2 = []
        return res

    def top(self):
        self.queue2 = self.queue1[:]
        for i in range(len(self.queue1)-1):
            self.queue1.pop()
        res = self.queue1 = self.queue2
        self.queue2 = []
        return res









