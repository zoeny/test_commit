# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/19 16:57
@month : 六月
@Author : mhm
@FileName: 6、判断链表是否存在环.py
@Software: PyCharm
'''
# 分析：使用双指针（快慢指针），一个指针每次移动一个节点，一个指针每次移动两个节点，如果存在环，那么这两个指针一定会相遇。
class LNode:
    def __init__(self,elem):
        self.elem = elem
        self.next = None

def hasCycle(LList):
    p1 = p2 = LList
    while p2 and p2.next: #当链表为空或者只有一个结点时，就不执行循环体里的程序，返回False
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True
    return False
        
if __name__ == '__main__':
    LList = LNode(1)
    p1 = LNode(2)
    p2 = LNode(3)
    p3 = LNode(4)
    p4 = LNode(5)
    p5 = LNode(6)
    LList.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p2
    print(hasCycle(LList))



