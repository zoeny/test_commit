# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/17 19:20
@month : 六月
@Author : mhm
@FileName: 2、返回字符组合数.py
@Software: PyCharm
'''

'''
"AAB"，可能的组合如下，返回 8
"A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"
'''
from collections import Counter
def numTilePossibilities(tiles):
    if len(tiles) == 0:
        return 0
    dt = dict(Counter(tiles))
    return dfs(dt)

def dfs(dt):
    sum = 0
    for k,v in dt.items():
        if v == 0:
            continue
        sum += 1
        dt[k] -= 1
        sum += dfs(dt)
        dt[k] += 1
    return sum

s = numTilePossibilities('AAB')
print(s)

'''返回数组子集'''
def substr(s):
    result = [[]]
    for i in range(len(s)):
        for j in range(len(result)):
            result.append(result[j]+[s[i]])
    return result

res = substr([1,2,3,4])
print(res)

'''返回字符的子集'''
import numpy
def strsub(s):
    result = [[]]
    a = numpy.array(list(s))
    for i in range(len(a)):
        for j in range(len(result)):
            result.append(result[j]+[a[i]])
    return result

a = strsub('aab')
print(a)



