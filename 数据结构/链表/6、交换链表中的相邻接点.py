# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/21 16:11
@month : 六月
@Author : mhm
@FileName: 6、交换链表中的相邻接点.py
@Software: PyCharm
'''
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self,head):
        p = head
        while p is not None and p.next is not None:
            tmp = p.val
            p.val = p.next.val
            p.next.val = tmp
            p = p.next.next
        return head

class Solution2:
    def swapPairs(self,head):
        if head == None or head.next == None:
            return head
        else:
            start = ListNode(0)
            start.next = head
            p = start
            q = start.next
            while q != None and q.next != None:
                p.next = q.next
                q.next = p.next.next
                p.next.next = q
                p = q
                q = q.next
            return start.next


