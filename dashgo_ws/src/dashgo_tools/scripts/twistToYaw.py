#!/usr/bin/env python
import tf

quaternion = (0.000000,0.000000,-0.006239,0.999981)
euler = tf.transformations.euler_from_quaternion(quaternion)
roll = euler[0]
pitch = euler[1]
yaw = euler[2]
print(yaw)
