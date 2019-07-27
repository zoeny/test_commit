# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/20 13:35
@month : 六月
@Author : mhm
@FileName: 3、归并两个有序链表(21).py
@Software: PyCharm
'''
'''
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

# 递归
def mergeTwoLists(l1,l2):
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next,l2)
        return l1
    else:
        l1.next = mergeTwoLists(l1,l2.next)
        return l2

#  第二种方法
class Solution:
    def mergeTwoLists1(self,l1,l2):
        head = ListNode(None)
        l3 = head
        while l1 != None and l2 != None:
            if l1.val >= l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 != None:
            head.next = l1
        if l2 != None:
            head.next = l2
        return l3.next





