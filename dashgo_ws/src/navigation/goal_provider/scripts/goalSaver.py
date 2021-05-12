#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.pose)
    coordinateX = data.pose.position.x
    coordinateY = data.pose.position.y
    quaternionX = data.pose.orientation.x
    quaternionY = data.pose.orientation.y
    quaternionZ = data.pose.orientation.z
    quaternionW = data.pose.orientation.w
    f= open("src/navigation/goal_provider/goals/goals.csv","a+")
    f.write("%f,%f,%f,%f,%f,%f\r\n" % (coordinateX, coordinateY, quaternionX, quaternionY, quaternionZ, quaternionW))
    f.close()
    
def listener():
    rospy.init_node('goal_listener', anonymous=True)

    rospy.Subscriber("move_base_simple/goal", PoseStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()