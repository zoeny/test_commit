# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 17:19
@month : 六月
@Author : mhm
@FileName: 1、用栈实现队列.py
@Software: PyCharm
'''
'''
栈的顺序为后进先出，而队列的顺序为先进先出。
使用两个栈实现队列，一个元素需要经过两个栈才能出队列，
在经过第一个栈时元素顺序被反转，
经过第二个栈时再次被反转，此时就是先进先出顺序。

使用栈实现队列的下列操作：
push(x) – 将一个元素放入队列的尾部。
pop() – 从队列首部移除元素。
peek() – 返回队列首部的元素。
empty() – 返回队列是否为空。

注意:

你只能使用标准的栈操作-- 也就是只有push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque (双端队列) 来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）

'''
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,x):
        self.stack1.append(x)

    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop()) # 将stack1中的数据放入stack2中
        res = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res

    def peek(self):
        return self.stack1[0]

    def empty(self):
        return not self.stack1











