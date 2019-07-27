# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/19 18:40
@month : 六月
@Author : mhm
@FileName: 7、最长子序列.py
@Software: PyCharm
'''

'''
eg:Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output:
"apple"
'''
'''
思路：
1）先把d中的元素按长度排序； 
2）将满足条件的且最长的字符串存在res中。引入flag变量和maxlen变量，来判断是否应该存入res中。 
3）如果len(res)为1，则输出。如果>1，则再将res进行排序，输出res[0].
'''
def findLongestWord(s,d):
    d.reverse()
    res = []
    maxlen = 0
    flag = 0
    d = sorted(d,key=lambda x:len(x))
    for item in d[::-1]:
        if flag == 1 and len(item) < maxlen:
            break
        i = j = 0
        while i < len(item) and j < len(s):
            if item[i] == s[j]:
                i += 1
            j += 1
        if i == len(item):
            flag = 1
            maxlen = len(item)
            res.append(item)
    if res == []:
        return ''
    elif len(res) == 1:
        return res[0]
    res.sort()
    return res[0]

print(findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"]))
















