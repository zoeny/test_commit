# -*- coding: utf-8 -*-
'''
@project: Pycharm_project
@Time : 2019/6/17 19:14
@month : 六月
@Author : mhm
@FileName: 1、输出所有匹配第1、2个单词后的第3个单词.py
@Software: PyCharm
'''

def findOcurrences(text,first,second):
    if text is None:
        return []
    words = text.split(' ')
    print(words)
    if len(words) <= 2:
        return []
    print('here')
    seqs = []
    seqs = [words[i+2] for i in range(len(words)-2) if words[i]==first and words[i+1]==second]
    return seqs

seq = findOcurrences('he is a so beautiful boy that many girls like he','a','so')
print(seq)
