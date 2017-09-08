# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:11:50 2017

@author: Spencersun
"""
num_digits = 0
num_letters = 0
input_str = "457ghj678bhj"
if input_str.isdigit() == True:
    num_digits = len(input_str)
    num_letters = 0
else:
    for i in range(len(input_str)):
        if input_str[i].isdigit() == True:
            num_digits += 1
        else:
            num_letters += 1
print ({"num_digits":num_digits})    
print ({"num_letters":num_letters})    
#d1 = input_str.isalpha()
#print (d2)
#print (d1)