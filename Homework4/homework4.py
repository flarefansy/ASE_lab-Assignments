# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 21:09:35 2017

@author: Spencersun
"""

from __future__ import print_function, division
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.cross_validation import train_test_split
import random

DATA_FILE = pd.read_csv('datatest.txt')
X_train, X_test, Y_train, Y_test = train_test_split(DATA_FILE[["Temperature", "Humidity", "Light", "CO2", "HumidityRatio"]].values, DATA_FILE["Occupancy"].values.reshape(-1, 1), random_state=42)

x = tf.placeholder(tf.float32, [None,5], name='X')
y = tf.placeholder(tf.float32, [None,1], name='Y')

w = tf.Variable(tf.zeros([5,1]), name='weights')
b = tf.Variable(tf.zeros([1]), name='bias')

prediction = tf.nn.sigmoid(tf.matmul(x,w) + b)
#loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=prediction,labels=y))
loss = tf.reduce_mean(tf.square(y-prediction, name='loss'))
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

correct_prediction = tf.equal(tf.round(prediction),y)
asss = tf.argmax(prediction,)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)
    for i in range(100):
        total_loss = 0
        _,l = sess.run([optimizer, loss], feed_dict={x: X_train, y: Y_train})
        total_loss += l
        #print('Epoch {0}: {1}'.format(i, total_loss / 1998))
        plt.plot(i, total_loss, 'co')
        print("Epoch:", "%04d" % i, "cost=", total_loss)
    prediction = sess.run(prediction, feed_dict={x: X_test})
    print("accuracy =", sess.run(accuracy, feed_dict={x: X_test, y: Y_test}))
    

plt.xlabel("Epoch")
plt.ylabel("Cost")
plt.show()

