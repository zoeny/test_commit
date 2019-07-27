# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 11:17
@month : 六月
@Author : mhm
@FileName: 9、分割链表.py
@Software: PyCharm
'''
# 题目描述：把链表分隔成 k 部分，每部分的长度都应该尽可能相同，排在前面的长度应该大于等于后面的。
'''
输入: 
root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self,root,k):
        ret = [None] * k
        length,move = 0,root
        while move:
            length += 1
            move = move.next
        avg,rem = length / k,length % k
        move,indexs = root,0
        while move:
            tmp = move
            pre = ListNode(0)
            pre.next = move
            num = 0
            while num < avg:
                pre,move = pre.next,move.next
                num += 1
            if rem:
                pre.move = pre.next,move.next
                rem -= 1
            pre.next = None
            ret[indexs] = tmp
            indexs += 1
        return ret
















