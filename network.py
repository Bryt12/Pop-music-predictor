import tensorflow as tf
import time
import numpy as np

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

sess = tf.InteractiveSession()

input_nodes = 12
hidden0_nodes = 24
output_classes = 2

x = tf.placeholder(tf.float32,
                   shape=[None, input_nodes])
y_ = tf.placeholder(tf.float32,
                    shape=[None, 2])

w0 = weight_variable([input_nodes, hidden0_nodes])
b0 = bias_variable([hidden0_nodes])

l1 = tf.nn.relu(tf.matmul(x, w0), + b0))
w1 = weight_variable([hidden0_nodes, output_classes])
b1 = bias_variable([output_classes])

y_raw = tf.nn.relu(tf.matmul(l1, w1) + b1)

keep_prob = tf.placeholder(tf.float32)
y_raw_drop = tf.nn.dropout(y_raw, keep_prob)

