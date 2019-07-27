# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/24 9:21
@month : 六月
@Author : mhm
@FileName: 10、链表元素按奇数偶数聚集.py
@Software: PyCharm
'''
'''
输入：1->2->3->4->5->NULL
输出：1->3->5->2->4->NULL
'''

'''
题目描述：给定一个单链表，把所有的奇数节点和偶数节点分别排在一起，
注意奇数偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self,head):
        if head == None or head.next == None or head.next.next == None:
            return head
        p = head.next # 偶数位
        q = head.next.next  # 奇数位
        head.next = q
        tmp = p
        while q.next: # q.next为偶数位，说明还有偶数位
            p.next = p.next.next
            p = p.next
            if q.next:
                q = q.next # while循环结束后q.next=None
            q.next = tmp # 奇数位连接到偶数位上
            p.next = None # 偶数位最后一位连接None
        return head

class Solution:
    def oddEvenList(self,head):
        A = []
        cp = head
        while cp:
            A.append(cp)
            cp = cp.next
        if len(A) <= 2:
            return head
        for i in range(len(A)-2):
            A[i].next = A[i+2]
        if len(A) % 2 == 0:
            A[-2].next = A[1]
            A[-1].next = None
        else:
            A[-1].next = A[1]
            A[-2].next = None
        return head




