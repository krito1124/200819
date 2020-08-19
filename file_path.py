# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:06:14 2020

@author: USER
"""

import os.path

if os.path.isfile('y.txt'):
    print('that is here')
    print("檔案94存在")
    
else:
    print('that is not here')
    file = open('y.txt','w')
    file.write('this is new one')
