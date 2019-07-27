# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/20 13:12
@month : 六月
@Author : mhm
@FileName: 2、链表反转(206).py
@Software: PyCharm
'''
'''
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

# 第一种方法：迭代
class Solution(object):
    def reverseList(self,head):
        if not head:
            return None
        p = head
        q = head.next
        p.next = None
        while q:
            r = q.next
            q.next = p
            p = q
            q = r
        return p

# 递归
class Solution2(object):
    def reverseList(self,head):
        if head == None and head.next == None:
            return head
        root = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return root

# 第三种方法:头插法
class Solution(object):
    def reverseList(self,head):
        cur = head
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            cur = next
        return pre