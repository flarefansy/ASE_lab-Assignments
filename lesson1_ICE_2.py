# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 19:30:30 2017

@author: Spencersun
"""

import math
input_number = int(input("Enter a number as radius of circle:"))
print ("The area of circle is %d, the circumference of circle is %d" % ((input_number**2)*math.pi, 2*input_number*math.pi))