import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy
import random

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Print four random samples from the training images
r=random.randint(0,len(mnist.train.images))
f, axarr = plt.subplots(2, 2, sharex=False)
axarr[0][0].imshow(numpy.reshape(mnist.train.images[r+0], (28, 28)))
axarr[0][0].set_title(numpy.where(mnist.train.labels[r+0]==1)[0][0])
axarr[0][1].imshow(numpy.reshape(mnist.train.images[r+1], (28, 28)))
axarr[0][1].set_title(numpy.where(mnist.train.labels[r+1]==1)[0][0])
axarr[1][0].imshow(numpy.reshape(mnist.train.images[r+2], (28, 28)))
axarr[1][0].set_title(numpy.where(mnist.train.labels[r+2]==1)[0][0])
axarr[1][1].imshow(numpy.reshape(mnist.train.images[r+3], (28, 28)))
axarr[1][1].set_title(numpy.where(mnist.train.labels[r+3]==1)[0][0])
f.subplots_adjust(hspace=0.3)
plt.show(block=True)

# Input variable definition and initialisation
x = tf.placeholder(tf.float32, [None, 784])

# Weights variable definition and initialisation
W = tf.Variable(tf.zeros([784, 10]))

# Bias variable definition and initialisation
b = tf.Variable(tf.zeros([10]))

# Model definition
y = tf.nn.softmax(tf.matmul(x, W) + b)