#!/usr/bin/env python2
import time
import rospy
import tf
from std_msgs.msg import String,Int32, Float32
from std_msgs.msg import Int32MultiArray as HoldingRegister
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import *
from nav_msgs.msg import Path
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import math
goal_path = [
    [6.5637345314,2.33047652245,0.000000,0.000000,0.00000,-0.710403,0.703795],#Ax,Ay,Az,qx,qy,qz,qw
    [13.525844574,3.52647829056,0.000000,0.000000,0.00000,-0.710403,0.703795]
]
station=[
    [7.05444955826,5.83697986603,0.000000,0.000000,0.00000,-0.710403,0.703795]
    ]
initial_position = None
move_base_status = 0 
class StateMachine:
    def __init__(self):
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.battery_status = rospy.Subscriber("batterystatus", Int32, self.batterycallback)
        self.distance_result = rospy.Publisher("distanceresult", Float32, queue_size=10) 
        self.mission_status = rospy.Subscriber("missionstatus",String ,self.missioncallback)
        self.plan_distance = rospy.Subscriber("/move_base/NavfnROS/plan", Path, self.distance_callback)
        self.robot_status = rospy.Publisher("robotstatus",String ,queue_size=10) 
        self.oldcoordinatex = 0.0
        self.oldcoordinatey = 0.0
        self.oldcoordinatez = 0.0
        self.distancegoal= 0.0
        self.cont=0
        self.batterypercentage=100
        self.newgoal = 0
        self.mission="Move" 
    def distance_callback(self,data):
        if self.distancegoal==0.0 and self.mission=="Move":
            for i in range(len(data.poses)-1):
                self.distancegoal += math.sqrt(pow((data.poses[i+1].pose.position.x - data.poses[i].pose.position.x),2) + pow((data.poses[i+1].pose.position.y - data.poses[i].pose.position.y), 2))
            self.distance_result.publish(self.distancegoal)

    def setServerFeedback(self, data):
        if len(data.status_list):
            move_base_status = data.status_list[0].status
    def batterycallback(self, msg):
        self.batterypercentage=msg.data
    def missioncallback(self, msg):
        self.mission=msg.data

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
            self.robot_status.publish("Success")
            self.newgoal +=1 if self.newgoal<=1 else 0
            self.distancegoal=0.0
        else:
            #Couldn't reach objective
            rospy.logwarn("Next coordinate")
            self.robot_status.publish("Failure")
            self.newgoal +=1 if self.newgoal<=1 else 0
            self.distancegoal=0.0
    def go_chargestation(self):
        socket_pub = rospy.Publisher("navBridgeServer/talker", String,queue_size=10) 
        rospy.Subscriber("move_base/status", GoalStatusArray, self.setServerFeedback)
        listener = tf.TransformListener()
        rospy.logwarn("Battery AI ready")
        angle = 70 * math.pi/180
        ax = station[0][0]
        ay = station[0][1]
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
            self.robot_status.publish("Success")
        else:
            #Couldn't reach objective
            rospy.logwarn("Next coordinate")
            self.robot_status.publish("Failure")
        self.distancegoal = 0

if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        r = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown() and robot.batterypercentage>=50:
            if robot.mission=="Charge":
                robot.robot_status.publish("Charging")
                #Goto Charge station
                rospy.logwarn("Charging")
                robot.go_chargestation()
            elif robot.mission=="Move":
                robot.robot_status.publish("Moving")
                #Goto next goal
                rospy.logwarn("Moving")
                robot.do_mission()
            else:
                #Free Robot 
                rospy.logwarn("Nothing")
                robot.robot_status.publish("Free")
            r.sleep()
    except rospy.ROSInterruptException:
        rospy.logerr("Navigation test finished.")
