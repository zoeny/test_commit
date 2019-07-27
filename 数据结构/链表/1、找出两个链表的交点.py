# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/19 9:28
@month : 六月
@Author : mhm
@FileName: 1、找出两个链表的交点.py
@Software: PyCharm
'''
'''
eg:
例如以下示例中 A 和 B 两个链表相交于 c1：

A:          a1 → a2
                    ↘
                      c1 → c2 → c3
                    ↗
B:    b1 → b2 → b3
但是不会出现以下相交的情况，因为每个节点只有一个 next 指针，也就只能有一个后继节点，而以下示例中节点 c 有两个后继节点。

A:          a1 → a2       d1 → d2
                    ↘  ↗
                      c
                    ↗  ↘
B:    b1 → b2 → b3        e1 → e2

要求时间复杂度为 O(N)，空间复杂度为 O(1)。如果不存在交点则返回 null。
设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。
当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；同样地，当访问 B 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点。
如果不存在交点，那么 a + b = b + a，以下实现代码中 l1 和 l2 会同时为 null，从而退出循环。
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
# 方法1：找到长度差(最耗时）
class Solution():
    def getIntersectionNode(self,headA,headB):
        a = b = 0
        h1 = headA
        h2 = headB
        while h1:
            h1 = h1.next
            a += 1
        while h2:
            h2 = h2.next
            b += 1
        h1 = headA
        h2 = headB
        if a >= b:
            for i in range(a-b):
                h1 = h1.next
        else:
            for i in range(b-a):
                h2 = h2.next
        while h1 and h2:
            if h1 is h2:
                break
            h1 = h1.next
            h2 = h2.next
        return h1

# 方法2：指针追逐
class Solution2(object):
    def getIntersectionNode(self,headA,headB):
        """
                将两个链表拼接在一起，p是headA->headB
                q是headB->headA
                这样p和q的长度一致，会在相交节点相遇
                要么就都返回None
                :param headA: ListNode
                :param headB: ListNode
                :return: ListNode
                """
        p = headA # p 4,1,8,4,5->5,0,1,8,4,5
        q = headB # q 5,0,1,8,4,5->4,1,8,4,5
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
'''
因为是找到相同的元素（id相同）所以之前的比较我用的是 is 而不是 ==
但这里可以用 ==
官方文档描述is为对象标示符（object identity），而==表示的是相等。
is的作用是用来检查对象的标示符是否一致，也就是两个对象在内存中的位置是否一样，
而==是用来检查两个对象是否相等。
'''

# 第三种方法：用集合（耗时居中）
class Solution3():
    def getintersectionNode(selfself,headA,headB):
        s = set()
        h1 = headA
        h2 = headB
        while h1:
            s.add(h1)
            h1 = h1.next
        while h2:
            if h2 in 2:
                break
            h2 = h2.next
        return h2



def stringToInt(input):
    return int(input)

def stringToListNode(intersectVal, listA, listB, skipA, skipB):
    '''输入生成list'''
    dummyRoot1 = ListNode(0)
    ptr1 = dummyRoot1
    dummyRoot2 = ListNode(0)
    ptr2 = dummyRoot2
    a = b = 0
    for number in listA:
        ptr1.next = ListNode(number)
        ptr1 = ptr1.next
        a += 1
        if a == skipA:
            break
    for number in listB:
        ptr2.next = ListNode(number)
        ptr2 = ptr2.next
        b += 1
        if b == skipB:
            break
    intersec = ptr1
    if intersectVal == 0:
        for i in range(a,len(listA)):
            ptr1.next = ListNode(listA[i])
            ptr1 = ptr1.next
    else:
        for i in range(a,len(listA)):
            ptr1.next = ptr2.next = ListNode(listA[i])
            ptr1,ptr2 = ptr1.next,ptr2.next
    return dummyRoot1.next,dummyRoot2.next,intersec.next

def listNodeToString(node):
    if not node:
        return '[]'
    result = ''
    while node:
        result += str(node.val) + ', '
        node = node.next
    return '['+result[:-2]+']'

def main():
    line1 = 8
    intersectVal = stringToInt(line1)
    listA = [4,1,8,4,5]
    listB = [5,0,1,8,4,5]
    line3 = 2
    skipA = stringToInt(line3)
    line4 = 3
    skipB = stringToInt(line4)
    headA,headB,intersec = stringToListNode(intersectVal,listA,listB,skipA,skipB)
    ret1 = Solution().getIntersectionNode(headA,headB)
    out = listNodeToString(ret1)
    if intersectVal>0 and ret1 is intersec:
        print('intersected at \"%d\"' % intersectVal)
    elif intersectVal == 0 and not ret1:
        print('No intersection')
    else:
        print('wrong output')
    print(out)

if __name__ == '__main__':
    main()



