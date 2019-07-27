# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/20 15:04
@month : 六月
@Author : mhm
@FileName: 5、删除链表的倒数第n个节点.py
@Software: PyCharm
'''

'''
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, 
the linked list becomes 1->2->3->5.
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFormEnd(self,head,n): # 我写的（错误）
        cur = head
        count = 0
        while cur:
            cur.next = cur.next
            count += 1
        cur.next = cur.next.next
        return cur

# 方法二
class Solution2:
    def removeNthFromEnd(self,head,n):
        l = []
        while head:
            l.append(head)
            head = head.next
        if len(l) == 1:
            return l[1]
        if len(l) == n:
            return l[1]
        if n == 1:
            l[-2].next = None
        else:
            l[-(n+1)].next = l[-(n-1)]
        return l[0]

class Solution3:
    def removeNth(self,head,n):
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        idx = length - n # 要删除的位置
        p = head # 重新赋值
        if idx == 0:
            return p.next
        for i in range(length):
            if i == idx - 1:
                p.next = p.next.next
                return head
            else:
                p = p.next


















