# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/27 20:57
@month : 六月
@Author : mhm
@FileName: 4、用栈实现括号匹配.py
@Software: PyCharm
'''
'''
"()[]{}"
Output : true
'''
def isValid(s): # 我的，能实现一部分
    si = ['(','{','[']
    stack = []
    for i in range(len(s)):
        if s[i] in si:
            stack.append(s[i])
        else:
            stack.pop()
    return stack == []

# 别人1
def isV1(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}','')
        s = s.replace('[]','')
        s = s.replace('()','')
    return s == ''

def isV2(s):
    l,r,stack = '({[',')}]',[]
    for item in s:
        if item in l:
            stack.append(item)
        else:
            if not stack or l.find(stack.pop()) != r.find(item):
                return False
    return not stack

def isV3(s):
    if not s:
        return True
    if len(s) & 1:
        return False
    for item in ['()','[]','{}']:
        if item in s:
            return isV3(s.replace(item,''))
    return False

def isV4(s):
    stack = []
    for i in s:
        if i in ['(','[','{']:
            stack.append(i)
        else:
            if not stack or {')':'(',']':'[','}':'{'}[i] != stack[-1]:
                return False
            stack.pop()
        return not stack

def isv5(s):
    stack = []
    dict = {']':'[','}':'{',')':'('}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []











