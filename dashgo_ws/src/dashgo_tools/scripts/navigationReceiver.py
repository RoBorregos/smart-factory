#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    if data.data == "done":
        pub = rospy.Publisher("cancel", String, queue_size=10)
        pub.publish(data.data)
    else:
        pub = rospy.Publisher('goTo', String, queue_size=10)
        pub.publish(data.data)
    
def listener():
    rospy.init_node('bridge_listener_nav', anonymous=True)

    rospy.Subscriber("navBridgeServer/listener", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
