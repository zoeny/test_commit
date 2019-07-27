# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/18 14:20
@month : 六月
@Author : mhm
@FileName: 4、回文字符串.py
@Software: PyCharm
'''
# 题目描述：可以删除一个字符，判断是否能构成回文字符串。
'''
eg:Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
'''
# 判断是否是回文字符
def validPal(s):
    n = len(s)
    cmp_time = (n+1)//2-1
    i = 0
    while i < cmp_time and s[i] == s[n-1-i]:
        i += 1
    if i == cmp_time:
        return True
    if s[i] == s[n-1-i-1]:
        while i < cmp_time and s[i] == s[n-1-i-1]:
            i += 1
    if s[i+1] == s[n-1-i]:
        while i < cmp_time and s[i+1] == s[n-1-i]:
            i += 1
    if i == cmp_time:
        return True
    return False

print(validPal('acbad'))

















