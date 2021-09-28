#!/usr/bin/env python
import rospy
import math
import tf
import geometry_msgs.msg

def saveGoal(trans, rot):
    print("Position saved: ", trans, rot)
    coordinateX = trans[0]
    coordinateY = trans[1]
    quaternionX = rot[0]
    quaternionY = rot[1]
    quaternionZ = rot[2]
    quaternionW = rot[3]
    f= open("saved_path.csv","a+")
    f.write("%f,%f,%f,%f,%f,%f\r\n" % (coordinateX, coordinateY, quaternionX, quaternionY, quaternionZ, quaternionW))
    f.close()

if __name__ == '__main__':
    rospy.init_node('goal_saver')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    trans, rot = None, None
    prev_trans, prev_rot = None, None
    while not trans:
        try:
            (trans,rot) = listener.lookupTransform('/map', '/base_link',rospy.Time(0))
            prev_trans = trans
            prev_rot = rot
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
    print("Position in map found.")
    saveGoal(trans, rot)
