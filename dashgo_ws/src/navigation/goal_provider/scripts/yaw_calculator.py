#!/usr/bin/env python
import tf

quaternion = (0.000000,0.000000,0.008553,0.999963)
euler = tf.transformations.euler_from_quaternion(quaternion)
roll = euler[0]
pitch = euler[1]
yaw = euler[2]
print(yaw)