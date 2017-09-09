# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:52:09 2017

@author: Spencersun
"""

input_str = ["music", "god", "computer"]
a = input_str[2]  
input_str.pop(2)
input_str.insert(0, a)

print (input_str)