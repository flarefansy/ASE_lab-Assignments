# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:04:25 2017

@author: Spencersun
"""

import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(5)

d = tf.add(a**2,b)
s = tf.multiply(d,c)

with tf.Session() as sess:
    print (sess.run(s))
