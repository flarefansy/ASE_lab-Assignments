# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 23:12:16 2017

@author: Spencersun
"""
k = {}
input_number = int(input("sample input:"))
for i in range(input_number):
    dic = {(i+1):(i+1)*(i+1)}
    k.update(dic)
print ("sample output:",k)