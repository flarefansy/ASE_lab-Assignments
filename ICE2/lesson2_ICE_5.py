# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:58:49 2017

@author: Spencersun
"""

heightinp = int(input("Enter the height of the board:"))
widthinp = int(input("Enter the width of the board: "))
for i in range(widthinp):
    if i%2==0:
        print ("|  "*heightinp)
    else:
        print ("---"*heightinp)
        
    