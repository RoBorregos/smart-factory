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
    [17.840215683, 5.21629333496,0.000000,0.000000,0.00000,-0.710403,0.703795],
    [1.832814,1.753299,0.000000,0.000000,0.00000,-0.710403,0.703795],#Ax,Ay,Az,qx,qy,qz,qw
    [5.425715,4.625706,0.000000,0.000000,0.00000,-0.000100,1.000000]
]
initial_position = None
move_base_status = 0
return_to_beginning = False
class StateMachine:
    def __init__(self):
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
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
    def do_mission(self, plcregisters):
        socket_pub = rospy.Publisher("navBridgeServer/talker", String) 
        rospy.Subscriber("move_base/status", GoalStatusArray, self.setServerFeedback)
        return_to_beginning = False
        listener = tf.TransformListener()
        trans, rot = None, None
        if(rr.registers[0]== 0):
            rospy.logwarn("Manual mode ready")
            angle = rr.registers[3] * math.pi/180
            ax = -float(str(plcregisters[1])[1:])/1000 if int(str(plcregisters[1])[:1]) == 1 and len(str(plcregisters[1])) == 5 else float(plcregisters[1])/1000
            ay = -float(str(plcregisters[2])[1:])/1000 if int(str(plcregisters[2])[:1]) == 1 and len(str(plcregisters[2])) == 5 else float(plcregisters[2])/1000
            a = [ ax, ay,0.000,0.000,0.000,0.000,0.000] #Ax,Ay,Az,qx,qy,qz,qw
            a[3] = 0.000
            a[4] = 0.000
            a[5] = math.sin(angle/2)
            a[6] = math.cos(angle/2)
            print(a)
            self.sendGoal1(a)
            socket_pub.publish("arrive")
        elif(rr.registers[0]== 1):
            rospy.logwarn("Auto mode ready")
            angle = rr.registers[6] * math.pi/180
            ax = -float(str(plcregisters[4])[1:])/1000 if int(str(plcregisters[4])[:1]) == 1 and len(str(plcregisters[4])) == 5 else float(plcregisters[4])/1000
            ay = -float(str(plcregisters[5])[1:])/1000 if int(str(plcregisters[5])[:1]) == 1 and len(str(plcregisters[5])) == 5 else float(plcregisters[5])/1000 
            a = [ ax, ay,0.000,0.000,0.000,0.000,0.000] #Ax,Ay,Az,qx,qy,qz,qw
            a[3] = 0.000
            a[4] = 0.000
            a[5] = math.sin(angle/2)
            a[6] = math.cos(angle/2)
            print(a)
            self.sendGoal1(a)
            socket_pub.publish("arrive")
        elif(rr.registers[0]== 2):
            rospy.logwarn("Stop mode ready")
    def test(self):
        socket_pub = rospy.Publisher("navBridgeServer/talker", String) 
        rospy.Subscriber("move_base/status", GoalStatusArray, self.setServerFeedback)
        a = goal_path[0]
        self.sendGoal1(a)
        socket_pub.publish("arrive")

        
if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        while not rospy.is_shutdown():
            # try:
            #     client =  ModbusClient("192.168.31.2",port=502)
            #     UNIT = 0x1
            #     conexion = client.connect()
            #     rospy.logwarn("Modbus connection ready")
            # except Exception as error:
            #     rospy.logwarn("Modbus connection error")
            #     rospy.logwarn(error)
            # try:
            #     rr = client.read_holding_registers(0,15,unit=UNIT)
            #     client.close()
            #     rospy.logwarn(rr.registers)
            #     rospy.logwarn("PLC-DASHGO working")
            #     robot.do_mission(rr.registers)
            #     rospy.sleep(1)
            # except Exception as error:
            #     rospy.logwarn("Reading registers not ready")
            #     rospy.logwarn(error)   
            try:
                robot.test()
            except Exception as error:
                rospy.logwarn(error)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
