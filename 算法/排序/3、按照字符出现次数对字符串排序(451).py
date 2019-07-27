# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/24 10:02
@month : 六月
@Author : mhm
@FileName: 3、按照字符出现次数对字符串排序(451).py
@Software: PyCharm
'''
'''
Input:
"tree"
Output:
"eert"
'''
# class Solution(object):
def frequencySort(s): # 我写的
    string = list(s)
    dict = {}
    result = ''
    for i in range(len(s)):
        if s[i] not in dict:
            dict[s[i]] = 1
        else:
            dict[s[i]] += 1
    out = sorted(dict.items(),key=lambda e:e[1],reverse=True)
    for k,v in out:
        result += k*v
    return result

class Solution:
    def frequencySort(self,s):
        dict = {}
        for j in range(len(s)):
            if s[j] in dict:
                dict[s[j]] += 1
            else:
                dict[s[j]] = 1
        list = [[] for i in range(len(s))]
        for key in dict:
            list[dict[key]-1].append(key)
        ans = ''
        for j in range(len(list)-1,-1,-1):
            if list[j] != []:
                for k in list[j]:
                    ans += (j+1)*k
        return ans















