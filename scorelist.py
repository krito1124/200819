# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:01:24 2020

@author: USER
"""

scores = []
maxscores = 0
minscores = 100
index=0
index2=0
total = 0

for i  in range(5):
    n = int(input("score"))
    name=input("name")
    scores.append(n)
    
    if n > maxscores:
        maxscores = n
        index=i
    if n < minscores:
        minscores = n
    total = total +n
        index=i
s = total/len(scores)
print('總分:',total)
print('平均',s)
print('最高分',maxscores)
print('最低分',minscores)
print("the highest,name[index])
print("the lowest,name[index2])