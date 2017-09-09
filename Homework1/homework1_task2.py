# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:10:11 2017

@author: Spencersun
"""

import string
input_str = input('Enter sting here:')
#input = 'bcdefghijklmna'
i = 0
result = 1
alphebet = string.ascii_lowercase[:]
for i in range(len(alphebet)):
    k = alphebet[i]
    if k not in input_str:
        result = 0
if result == 0:
    print ("This string doesn't contain all letters of the alphabet.")
else: 
    print ("This string contains all letters of the alphabet.")
