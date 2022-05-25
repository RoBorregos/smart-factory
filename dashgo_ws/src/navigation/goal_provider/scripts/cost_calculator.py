#!/usr/bin/env python
import rospy
import math
from nav_msgs.msg import Path

def callback(path):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", path)
    prev_x = path.poses[0].pose.position.x
    prev_y = path.poses[0].pose.position.y
    cost = 0

    for pose in path.poses[1:]:
        cost+= math.sqrt(pow((pose.pose.position.x - prev_x),2)+ pow((pose.pose.position.y - prev_y),2))
        prev_x = pose.pose.position.x
        prev_y = pose.pose.position.y

    rospy.logwarn('Current cost: {:.2f}'.format(cost))
    
def listener():
    rospy.init_node('cost_calculator', anonymous=True)

    rospy.Subscriber("/path_test_server", Path, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()