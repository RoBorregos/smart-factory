#!/usr/bin/env python2
import time
import rospy
import tf
from std_msgs.msg import String
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

places = [
    [0.894217,0.245097,0.000000,0.000000,0.698344,0.715762],
    [1.787545,-1.220013,0.000000,0.000000,0.049991,0.998750],
    [2.093635,-2.358750,0.000000,0.000000,-0.061845,0.998086],
    [1.116934,-3.681892,0.000000,0.000000,0.997756,0.066959],
] 

place_dict = {
    "couch": 0,
    "closet": 1,
    "bathroom": 2,
    "kitchen": 3
}

initial_position = None

move_base_status = 0

return_to_beginning = False

def setServerFeedback(data):
    if len(data.status_list):
        move_base_status = data.status_list[0].status

def movebase_client(place):
    socket_pub = rospy.Publisher("navBridgeServer/talker", String) 
    return_to_beginning = False
    place = place.data
    if len(place) == 1 and int(place) in range(0,11):
        goal = places[int(place)]
    elif place in place_dict:
        goal = places[place_dict[place]]
    else:
        print("Invalid goal!")
        return False
    sendGoal(goal)
    socket_pub.publish("arrive")
 
    print("Going to goal")
    pub = rospy.Publisher('cmd_vel', Twist)
    move_cmd = Twist()
    move_cmd.linear.x = 0
    move_cmd.linear.y = 0
    move_cmd.linear.x = 0
    move_cmd.angular.z = -0.3
    speed = 0.3
    rate = rospy.Rate(10)

    print("Searching")

    # girar todo izquierda
    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(6):
        pub.publish(move_cmd)
        rate.sleep()

    # girar todo derecha
    move_cmd.angular.z = 0.3
    now = rospy.Time.now()
    while rospy.Time.now() < now + rospy.Duration.from_sec(12) and not return_to_beginning:
        pub.publish(move_cmd)
        rate.sleep()
    print("Returning")    
    socket_pub.publish("return") 

    sendGoal(initial_position)
    socket_pub.publish("done") 

def sendGoal(goal_position):
    global move_base_status
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    print("Client exists")
    goal = MoveBaseGoal() 
    goal.target_pose.header.frame_id = "/map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose = Pose(Point(goal_position[0], goal_position[1], 0.0), Quaternion(goal_position[2],goal_position[3], goal_position[4], goal_position[5]))
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

def cancel_moveBase(data):
    return_to_beginning = True

if __name__ == '__main__':
    rospy.init_node('goToNavigation', anonymous=0)
    listener = tf.TransformListener()
    trans, rot = None, None
    while not trans:
        try:
            (trans,rot) = listener.lookupTransform('/map', '/base_link',rospy.Time(0))
            trans = trans
            rot = rot
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
    print("Initial position in map found.")
    initial_position = [trans[0], trans[1], rot[0], rot[1], rot[2], rot[3]]
    rospy.Subscriber("goTo", String, movebase_client)
    rospy.Subscriber("cancel", String, cancel_moveBase)
    rospy.Subscriber("move_base/status", GoalStatusArray, setServerFeedback)
    rospy.spin()
