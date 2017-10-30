# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:59:39 2017

@author: Spencersun
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd
#from mpl_toolkits.mplot3d import Axes3DZ

DATA_FILE = 'print_orders.xls'

book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
data[:,0] = data[:,0]/1000
data[:,2] = data[:,2]/1000
n_samples = sheet.nrows - 1

X1 = tf.placeholder(tf.float32, name='X1')
X2 = tf.placeholder(tf.float32, name='X2')
Y = tf.placeholder(tf.float32, name='Y')

w1 = tf.Variable(0.0, name='weights1')
w2 = tf.Variable(0.0, name='weights2')
b = tf.Variable(0.0, name='bias')

Y_predicted = w1*X1 + w2*X2 + b
loss = tf.square(Y - Y_predicted, name='loss')
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)
    for i in range(100):
        total_loss = 0
        for x1, x2, y in data:
            # Session runs train_op and fetch values of loss
            Y_predicted, l = sess.run([optimizer, loss], feed_dict={X1: x1, X2: x2, Y: y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))
    #writer.close()
    #w, b = sess.run([w, b])

#X1, X2, Y = data.T[0], data.T[1], data.T[2]
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(X1, X2, X1 * w1 + X2 * w2 + b, 'bo', label='predicted Y')
#ax.scatter(X1, X2, Y, 'ko', label='Real Y')
#plt.legend()
#plt.show() 
    