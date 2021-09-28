#!/usr/bin/env python2
import time
import sys
import rospy
import tf
from std_msgs.msg import String
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

places = [
    [0.115000,0.000000,0.000000,0.000000,0.000000,1.000000],
    [0.048316,-0.334333,0.000000,0.000000,-0.721069,0.692863],
    [2.452428,-0.340753,0.000000,0.000000,-0.005907,0.999983],
    [3.312724,-0.696531,0.000000,0.000000,-0.003698,0.999993],
    [2.982722,1.268492,0.000000,0.000000,0.158861,0.987301],
    [3.698247,1.887707,0.000000,0.000000,0.453090,0.891465],
    [-0.178596,0.935838,0.000000,0.000000,0.630688,0.776036],
    [-0.050914,0.259309,0.000000,0.000000,0.007334,0.999973]
]  

place_dict = {
    "lobby": 0,
    "closet": 1,
    "bathroom": 2,
    "kitchen": 3
}

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
    rospy.init_node('navSendGoal', anonymous=0)
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Please state a position in the map.")
        exit(0)
    place = sys.argv[1]
    if len(place) == 1 and int(place) in range(0,7):
        goal = places[int(place)]
    elif place in place_dict:
        goal = places[place_dict[place]]
    else:
        print("Invalid goal!")
        exit(0)
    sendGoal(goal)

