# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:19:31 2017

@author: Spencersun
"""

import numpy as np

matrix = np.random.random((10,10))
matrix_max = np.max(matrix)
matrix_min = np.min(matrix)
print (matrix_max, matrix_min)