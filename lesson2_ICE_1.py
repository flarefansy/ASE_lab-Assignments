# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:04:11 2017

@author: Spencersun
"""

input_str = "sdfbhjbsdijdnisjnvidjv"
result = {}
for i in range(len(input_str)):
    dict = {input_str[i]:input_str.count(input_str[i])}
    result.update(dict)
print (result)