# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:24:38 2017

@author: Spencersun
"""
result = {}
input = ["geh", "asde", "asdbhujb"]
for i in range(len(input)):
    diction = {len(input[i]):input[i]}
    result.update(diction)
print (result)