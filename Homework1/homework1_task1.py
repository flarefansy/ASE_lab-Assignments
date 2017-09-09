# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:22:09 2017

@author: Spencersun
"""

#input_str = "hello hey hey hello tell me is all me"
input = open("test.txt")
input_str = input.read()
word = input_str.split()
result = {}
for i in range(len(word)):
    dict = {word[i]:word.count(word[i])}
    result.update(dict)
print (result)
