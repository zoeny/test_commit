# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/22 9:29
@month : 六月
@Author : mhm
@FileName: 8、回文链表.py
@Software: PyCharm
'''
'''
输入: 1->2->2->1 
输出: true
'''
# 方法一
class Solution:
    def isPalindrome(self,head):
        if head is None or head.next is None:
            return True
        l = []
        p = head
        while p.next:
            l.append(p.val)
            p = p.next
        l.append(p.val)
        return l == l[::-1]

# 方法二：用双指针
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution2:
    def isPalindrome(self,head):
        if head is None or head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        fast = slow = q = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        def reverse_list(head):
            if head is None:
                return head
            cur = head
            pre = None
            nxt = cur.next
            while nxt:
                cur.next = pre
                pre = cur
                cur = nxt
                nxt = nxt.next
            cur.next = pre
            return cur
        p = reverse_list(slow.next)
        while p.next:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return p.val == q.val













