#!/usr/bin/env python2
import time
import rospy
import tf
from std_msgs.msg import String
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import math
goal_path = [
    [7.11645317078,6.30571556091,0.000000,0.000000,0.00000,-0.710403,0.703795],
    [6.56161832809,2.42692947388,0.000000,0.000000,0.00000,-0.710403,0.703795],#Ax,Ay,Az,qx,qy,qz,qw
    [5.425715,4.625706,0.000000,0.000000,0.00000,-0.710403,0.703795]
]
initial_position = None
move_base_status = 0
return_to_beginning = False
class StateMachine:
    def __init__(self):
        self.client = actionlib.SimpleActionClient('dashgo_0/move_base', MoveBaseAction)
    def setServerFeedback(self, data):
        if len(data.status_list):
            move_base_status = data.status_list[0].status
    def sendGoal1(self,goal_position):
        global move_base_status
        self.client.wait_for_server()
        print("Client exists")
        goal = MoveBaseGoal() 
        goal.target_pose.header.frame_id = "/map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(goal_position[0], goal_position[1], goal_position[2]), Quaternion(goal_position[3],goal_position[4], goal_position[5], goal_position[6]))
        self.client.send_goal(goal)
        wait = self.client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return self.client.get_result()
    def test(self):
        socket_pub = rospy.Publisher("navBridgeServer/talker", String) 
        rospy.Subscriber("dashgo_0/move_base/status", GoalStatusArray, self.setServerFeedback)
        a = goal_path[0]
        self.sendGoal1(a)
        socket_pub.publish("arrive")

        
if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        while not rospy.is_shutdown():
            try:
                robot.test()
            except Exception as error:
                rospy.logwarn(error)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
