# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:28:19 2017

@author: Spencersun
"""

from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation as cv

iris = datasets.load_iris()
x = iris.data
y = iris.target
splits = cv.train_test_split(x, y, test_size=0.2)
x_train, x_test, y_train, y_test = splits
gnb = GaussianNB()
y_pred = gnb.fit(x_train, y_train).predict(x_test)
print ((y_test == y_pred).sum())
print (len(y_test))
print('%.2f%%' % (((y_test == y_pred).sum()/len(y_test))*100))
