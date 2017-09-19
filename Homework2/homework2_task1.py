# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 23:23:55 2017

@author: Spencersun
"""

input_str = "hello world and practice makes perfect and hello world again"
word = input_str.split()
lists = list(set(word)) 
lists.sort()
print (lists)