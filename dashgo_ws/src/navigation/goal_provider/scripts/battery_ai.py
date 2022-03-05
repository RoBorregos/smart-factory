#!/usr/bin/env python2
import time
import rospy
import tf
from std_msgs.msg import String,Int32
from std_msgs.msg import Int32MultiArray as HoldingRegister
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import math
goal_path = [
    [7.05444955826,5.83697986603,0.000000,0.000000,0.00000,-0.710403,0.703795],#Ax,Ay,Az,qx,qy,qz,qw
    [6.5637345314,2.33047652245,0.000000,0.000000,0.00000,-0.710403,0.703795],
    [13.525844574,3.52647829056,0.000000,0.000000,0.00000,-0.710403,0.703795]
]
initial_position = None
move_base_status = 0 
class StateMachine:
    def __init__(self):
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.battery_status = rospy.Subscriber("batterystatus", Int32, self.batterycallback)
        self.oldcoordinatex = 0.0
        self.oldcoordinatey = 0.0
        self.oldcoordinatez = 0.0
        self.cont=0
        self.batterypercentage=100
        self.newgoal = 0
    def setServerFeedback(self, data):
        if len(data.status_list):
            move_base_status = data.status_list[0].status
    def batterycallback(self, msg):
        self.batterypercentage=msg.data

    def sendGoal1(self,goal_position):
        global move_base_status
        self.client.wait_for_server()
        rospy.logwarn("Client exists")
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
    def do_mission(self):
        socket_pub = rospy.Publisher("navBridgeServer/talker", String,queue_size=10) 
        rospy.Subscriber("move_base/status", GoalStatusArray, self.setServerFeedback)
        listener = tf.TransformListener()
        rospy.logwarn("Battery AI ready")
        angle = 70 * math.pi/180
        ax = goal_path[self.newgoal][0]
        ay = goal_path[self.newgoal][1]
        rospy.logwarn(ax)
        rospy.logwarn(self.newgoal)
        rospy.logwarn(goal_path[0][0])
        a = [ ax, ay,0.000,0.000,0.000,0.000,0.000] #Ax,Ay,Az,qx,qy,qz,qw
        a[3] = 0.000
        a[4] = 0.000
        a[5] = math.sin(angle/2)
        a[6] = math.cos(angle/2)
        status = self.sendGoal1(a)
        if (status):
            #Success mobile robot , change coordinate
            rospy.logwarn("I arrive")
            socket_pub.publish("I arrive")
            self.newgoal +=1 if self.newgoal<=2 else 0
        else:
            #Couldn't reach objective
            rospy.logwarn("Next coordinate")
            self.newgoal +=1 if self.newgoal<=2 else 0
        
if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        r = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown() and robot.batterypercentage>=50:
            rospy.logwarn("PLC-DASHGO Battery AI working")
            robot.do_mission()
            r.sleep()
    except rospy.ROSInterruptException:
        rospy.logerr("Navigation test finished.")
