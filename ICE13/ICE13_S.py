
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
import tensorflow as tf

def load_CIFAR_batch(filename):
   with open(filename, 'rb') as f:
     datadict = pickle.load(f,encoding='latin1')
     X = datadict['data']
     Y = datadict['labels']
     X = X.reshape(10000, 3, 32,32).transpose(0,2,3,1).astype("float")
     Y = np.array(Y)
     return X, Y

def load_CIFAR10(ROOT):
    xs = []
    ys = []
    for b in range(1,6):
        f = os.path.join(ROOT, 'data_batch_%d' % (b, ))
        X, Y = load_CIFAR_batch(f)
        xs.append(X)　　
        ys.append(Y)    
    Xtr = np.concatenate(xs)
    Ytr = np.concatenate(ys)
    del X, Y
    Xte, Yte = load_CIFAR_batch(os.path.join(ROOT, 'test_batch'))
    return Xtr, Ytr, Xte, Yte

# Import data
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

# Variables
with tf.name_scope('inputs'):
    x = tf.placeholder("float", [None, 784],name='x')
    y_ = tf.placeholder("float", [None, 10],name='y')

with tf.name_scope('layer'):
    with tf.name_scope('Weights'):
        w_enc = tf.Variable(tf.random_normal([784, 625], mean=0.0, stddev=0.05),name='w_enc')
        w_dec = tf.Variable(tf.random_normal([625, 784], mean=0.0, stddev=0.05),name='w_dec')
    with tf.name_scope('biases'):    
        b_enc = tf.Variable(tf.zeros([625]),name='b_enc')
        b_dec = tf.Variable(tf.zeros([784]),name='b_dec')


# Create the model
def model(X, w_e, b_e, w_d, b_d):
    encoded = tf.sigmoid(tf.matmul(X, w_e) + b_e)
    decoded = tf.sigmoid(tf.matmul(encoded, w_d) + b_d)

    return encoded, decoded


encoded, decoded = model(x, w_enc, b_enc, w_dec, b_dec)

# Cost Function basic term
with tf.name_scope('cost'):
    cross_entropy = -1. * x * tf.log(decoded) - (1. - x) * tf.log(1. - decoded)
    loss = tf.reduce_mean(cross_entropy)
    train_step = tf.train.AdamOptimizer(0.01).minimize(loss)

# Train
init = tf.initialize_all_variables()
tf.summary.scalar("cost", loss)
merged_summary = tf.summary.merge_all()
writer = tf.summary.FileWriter('D://log')
saver = tf.train.Saver()

load_CIFAR_Labels("/cifar-10-batches-py/batches.meta")
imgX, imgY = load_CIFAR_batch("/data/cifar-10-batches-py/data_batch_1")

with tf.Session() as sess:
    sess.run(init)
    writer.add_graph(sess.graph)
    print('Training...')
    for i in range(4001):
        batch_xs, batch_ys = mnist.train.next_batch(128)
        train_step.run({x: batch_xs, y_: batch_ys})
        s = sess.run(merged_summary, {x: batch_xs, y_: batch_ys})
        writer.add_summary(s,i)

        if i % 1000 == 0:
            train_loss = loss.eval({x: batch_xs, y_: batch_ys})
            print('  step, loss = %6d: %6.3f' % (i, train_loss))

    # generate decoded image with test data
    test_fd = {x: mnist.test.images, y_: mnist.test.labels}
    decoded_imgs = decoded.eval(test_fd)
    print('loss (test) = ', loss.eval(test_fd))

x_test = mnist.test.images

n = 10  # how many digits we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # display original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.savefig('simple_ae.png')
