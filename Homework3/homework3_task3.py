# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:07:19 2017

@author: Spencersun
"""

from sklearn import svm
from sklearn import datasets
from sklearn import cross_validation as cv

digitsdataset=datasets.load_digits()
x=digitsdataset.data
y=digitsdataset.target
splits = cv.train_test_split(x[:,:2], y, test_size=0.2)
x_train, x_test, y_train, y_test = splits

#linear model
linearmodel = svm.SVC(C=0.9,kernel='linear',decision_function_shape='ovr')
linearmodel.fit(x_train,y_train)
y_pred = linearmodel.predict(x_test)
print('%.2f%%' % (((y_test == y_pred).sum()/len(y_test))*100))

#rbf model
rbfmodel = svm.SVC(C=1,kernel='rbf',decision_function_shape='ovr')
rbfmodel.fit(x_train,y_train)
y_pred = rbfmodel.predict(x_test)
print('%.2f%%' % (((y_test == y_pred).sum()/len(y_test))*100))
