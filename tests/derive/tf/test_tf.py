import numpy as np
import tensorflow as tf

a=np.zeros((2,4))
print(a)

b=np.ones((2,4))
print(b)

c = np.eye(3) #创建单位对角的数组
print(c)

#Matrix

a = np.mat(([1,2],[3,4]))
print(a)
print(a.T)
print(a.I)  #求逆

b = np. mat(([5,6],[7,8]))
print(a*b)


x = tf.constant(10)
print(x)

x = tf.Variable(tf.ones([3,3]))
print(x)
y = tf.Variable(tf.zeros([3,3]))
print(y)
init = tf.global_variables_initializer()
print(x)
print(y)
x=tf.placeholder(tf.float32, [None,784])
print(x)

#在Tensorflow中，每个变量都 是一个tensor对象，对象间的运算统一称之操作OP,
#TensorFlow不会去一条条执行各个操作，而是把所有的操作都放入到一个图(graph)中,图中的每一个结点就是一个操作，然后将
#整个graph的计算过程交给一个TensorFlow的session, 此session可以运行整个计算过程

x = tf.Variable(3)
y = tf.Variable(5)
z=x+y
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(z))

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
output = tf.multiply(x,y,'multiply')

with tf.Session() as sess:
    print( sess.run([output],feed_dict={input:[7.], input:[2.]}))