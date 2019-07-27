# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/7/4 18:50
@month : 七月
@Author : mhm
@FileName: 2、校对程序（头条）.py
@Software: PyCharm
'''
'''
实现一个单词校对程序，实现以下几个功能：

如果有三个同样的字母连在一起，则需要去掉一个，如’helllo’ -> ‘hello’
如果有两对同样的字母(AABB型)连在一起，去掉第二对的一个字母，如’helloo’ -> ‘hello’
上面的规则都必须优先从左到右匹配，如’AABBCC’，要先处理第一个’AABB’，结果为’AABCC’
输入描述：
第一行包含一个数字n，表示本次用例包括多少个待校验的字符串
之后n行，每行为一个待校验的字符串。
输出描述：
n行，每行包括一个被修复后的字符串
示例1：
输入：
2
helloo
wooooooooow
输出：
hello
woow

思路：
题意其实还是比较明确的，对于当前遍历的字符v，只要分别判断他与前一个字符p，前前一个字符pp,前前前一个字符ppp之间的关系即可，若满足两种规则中的任意一种，则删去v字符。
这里我使用队列实现，我觉着这样写起来会更清晰一点（也可以使用指针）
'''
import collections
n = int(input())
def solve(s):
    if len(s)<=3:
        return s
    res = []
    s = list(s)
    q = collections.deque(s[2:])
    # 尝试不要pppp
    pp,p = s[0],s[1]
    ppp = None
    while q:
        v = q.popleft()
        # 第一种错误情况
        if v == p == pp:
            continue
        if ppp:
            # 第二种错误情况
            if v == p and pp == ppp:
                continue
            res.append(ppp)
        ppp,pp,p = pp,p,v
    res.extend([ppp,pp,p])
    return ''.join(res)

for _ in range(n):
    s = input()
    print(solve(s))













