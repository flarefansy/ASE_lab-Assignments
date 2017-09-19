# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 00:05:11 2017

@author: Spencersun
"""

import numpy as np

vector = np.random.randn(5)
re = np.where(vector==np.max(vector))
print (vector)
print (re[0][0])
a = np.delete(vector, re[0][0])
result = np.insert(a, re[0][0], 100)
print (result)
