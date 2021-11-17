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
    [7.05444955826,5.83697986603,0.000000,0.000000,0.00000,-0.710403,0.703795],#Ax,Ay,Az,qx,qy,qz,qw
    [6.5637345314,2.33047652245,0.000000,0.000000,0.00000,-0.710403,0.703795],
    [13.525844574,3.52647829056,0.000000,0.000000,0.00000,-0.710403,0.703795]
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
    def test(self,index):
        socket_pub = rospy.Publisher("navBridgeServer/talker", String) 
        rospy.Subscriber("dashgo_0/move_base/status", GoalStatusArray, self.setServerFeedback)
        a = goal_path[index]
        rospy.logwarn(index)
        self.sendGoal1(a)
        socket_pub.publish("arrive")

        
if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        while not rospy.is_shutdown():
            try:
                client =  ModbusClient("192.168.100.23",port=502)
                UNIT = 0x1
                conexion = client.connect()
                rospy.logwarn("Modbus connection ready")
            except Exception as error:
                rospy.logwarn("Modbus connection error")
                rospy.logwarn(error)
            try:
                rr = client.read_holding_registers(0,15,unit=UNIT)
                client.close()
                rospy.loginfo("PLC Registers:")
                rospy.logwarn("PLC Registers:")
                rospy.logwarn(rr.registers)
                rospy.logwarn("Dashgo Rviz working")
                #robot.do_mission(rr.registers)
                rospy.sleep(1)
            except Exception as error:
                rospy.logwarn("Reading registers not ready")
                rospy.logwarn(error)   
            # try:
            #     for i in range(len(goal_path)):
            #         robot.test(i)
            # except Exception as error:
            #     rospy.logwarn(error)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
