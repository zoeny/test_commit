# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/20 14:43
@month : 六月
@Author : mhm
@FileName: 4、从有序链表中删除重复节点.py
@Software: PyCharm
'''

'''
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self,head): # 我写的
        if head == None and head.next == None:
            return None
        l1 = head
        if l1.val == head.next:
            l1.next = head.next.next
        else:
            l1.next = head.next
        return head

class Solution2:
    def deleteDuplicates(self,head):
        current = head
        while current != None and current.next != None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head





















