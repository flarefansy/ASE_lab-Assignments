# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 01:09:56 2017

@author: Spencersun
"""

import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
upper = 0
down = 0 
Y_pred = []
X_mean = np.mean(X)
Y_mean = np.mean(Y)
for i in range(len(X)):
    K = (X_mean-X[i])*(Y_mean-Y[i])
    G = np.square(X_mean-X[i])    
    upper = K + upper
    down = G + down
b_1 = upper/down
b_0 = Y_mean - b_1*X_mean
Y_pred = b_0+np.multiply(b_1,X)
#linear_mod = linear_model.LinearRegression()
#X = np.reshape(X, (len(X), 1))  # converting to matrix of n X 1
#Y = np.reshape(Y, (len(Y), 1))
#linear_mod.fit(X, Y)  # fitting the data points in the model
plt.scatter(X, Y, color='yellow')  # plotting the initial datapoints
plt.plot(X, Y_pred, color='blue', linewidth=3)
#plt.plot(X, linear_mod.predict(X), color='blue', linewidth=3)  # plotting the line made by linear regression
plt.show()
