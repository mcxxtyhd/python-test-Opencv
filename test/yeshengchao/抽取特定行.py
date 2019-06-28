# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 11:37:56 2019

@author: Administrator
"""

f = open('D:\CCbondJ\CCBJ3.txt','r')
lines = f.readlines()
for lines in lines:
   if "Generated" in lines:
     print(lines)