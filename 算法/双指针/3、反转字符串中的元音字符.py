# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/18 12:54
@month : 六月
@Author : mhm
@FileName: 3、反转字符串中的元音字符.py
@Software: PyCharm
'''

# 分析：使用双指针指向待反转的两个元音字符，一个指针从头向尾遍历，一个指针从尾到头遍历。
# eg：Given s = "leetcode", return "leotcede".
# 元音：aioue
def reverseVowels(s):
    vowe = ['a','i','o','u','e']
    i,j = 0,len(s)-1    ## 这一步就是设置指针，相当重要，在思路里
    while i < j:
        if s[i] in vowe and s[j] in vowe and s[i] != s[j]:
            tmp1 = s[i]
            tmp2 = s[j]
            s = s[:i] + tmp2 + s[(i+1):j] + tmp1 + s[(j+1):]
            return s
        else:
            i += 1
            j -= 1

print(reverseVowels('leetcode'))





