#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.pose)
    coordinateX = data.pose.pose.position.x
    coordinateY = data.pose.pose.position.y
    quaternionX = data.pose.pose.orientation.x
    quaternionY = data.pose.pose.orientation.y
    quaternionZ = data.pose.pose.orientation.z
    quaternionW = data.pose.pose.orientation.w
    f= open("src/navigation/goal_provider/goals/goals.csv","a+")
    f.write("%f,%f,%f,%f,%f,%f\r\n" % (coordinateX, coordinateY, quaternionX, quaternionY, quaternionZ, quaternionW))
    f.close()
    
def listener():
    rospy.init_node('goal_listener', anonymous=True)

    rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()