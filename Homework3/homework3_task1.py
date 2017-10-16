# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:16:14 2017

@author: Spencersun
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn import cross_validation as cv

iris = datasets.load_boston()
x = iris.data[:,np.newaxis,2]
y = iris.target
splits = cv.train_test_split(x, y, test_size=0.2)
x_train, x_test, y_train, y_test = splits
regr = linear_model.LinearRegression()
y_pred = regr.fit(x_train, y_train).predict(x_test)
plt.scatter (x_test, y_test, color='black')
plt.plot (x_test, y_pred, color='blue', linewidth=5)
