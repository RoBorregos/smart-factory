#!/usr/bin/env python
import rospy
import actionlib
from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import math
# goal_path = [
#     [1.832814,1.753299,0.000000,0.000000,-0.710403,0.703795],
#     [5.425715,4.625706,0.000000,0.000000,-0.000100,1.000000]
# ]
class StateMachine:
    def __init__(self):
        self.client = actionlib.SimpleActionClient('/dashgo_0/move_base', MoveBaseAction)
    def do_mission(self, plcregisters):
        self.client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "/map"
        goal.target_pose.header.stamp = rospy.Time.now()

        if(rr.registers[0]== 0):
            rospy.logwarn("Manual mode ready")
            angle = rr.registers[3] * math.pi/180
            ax = -float(str(plcregisters[1])[1:])/1000 if int(str(plcregisters[1])[:1]) == 1 and len(str(plcregisters[1])) == 5 else float(plcregisters[1])/1000
            ay = -float(str(plcregisters[2])[1:])/1000 if int(str(plcregisters[2])[:1]) == 1 and len(str(plcregisters[2])) == 5 else float(plcregisters[2])/1000
            a = [ ax, ay,0.000] #Ax,Ay,Az
            qw = math.cos(angle/2)
            qx = 0.000
            qy = 0.000
            qz = math.sin(angle/2)
	    rospy.logwarn(a[0])
	    rospy.logwarn(a[1])
	    rospy.logwarn(a[2])
	    rospy.logwarn(angle)
            rospy.logwarn(qx)
	    rospy.logwarn(qy)
	    rospy.logwarn(qz)
            rospy.logwarn(qw)
            goal.target_pose.pose = Pose(Point(a[0], a[1],  a[2]), Quaternion(qx,qy,qz,qw))
            self.client.send_goal(goal)
            print("Goal to dashgo 0 sent")
            wait = self.client.wait_for_result()
            if not wait:
                rospy.logerr("Action server not available!")
                rospy.signal_shutdown("Action server not available!")
                return None
            else:
                return self.client.get_result()
        else:
            rospy.logwarn("Auto mode ready")
            angle = rr.registers[6] * math.pi/180
            ax = -float(str(plcregisters[4])[1:])/1000 if int(str(plcregisters[4])[:1]) == 1 and len(str(plcregisters[4])) == 5 else float(plcregisters[4])/1000
            ay = -float(str(plcregisters[5])[1:])/1000 if int(str(plcregisters[5])[:1]) == 1 and len(str(plcregisters[5])) == 5 else float(plcregisters[5])/1000 
            a = [ ax, ay,0.000] #Ax,Ay,Az
            qw = math.cos(angle/2)
            qx = 0.000
            qy = 0.000
            qz = math.sin(angle/2)
            rospy.logwarn(a[0])
            rospy.logwarn(a[1])
            rospy.logwarn(a[2])
            rospy.logwarn(angle)
            rospy.logwarn(qx)
            rospy.logwarn(qy)
            rospy.logwarn(qz)
            rospy.logwarn(qw)
            goal.target_pose.pose = Pose(Point(a[0], a[1],  a[2]), Quaternion(qx,qy,qz,qw))
            self.client.send_goal(goal)
            print("Goal to dashgo 0 sent")
            wait = self.client.wait_for_result()
            if not wait:
                rospy.logerr("Action server not available!")
                rospy.signal_shutdown("Action server not available!")
                return None
            else:
                return self.client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        while not rospy.is_shutdown():
            try:
                client =  ModbusClient("192.168.31.2",port=502)
                UNIT = 0x1
                conexion = client.connect()
                rospy.logwarn("Modbus connection ready")
            except Exception as error:
                rospy.logwarn("Modbus connection error")
                rospy.logwarn(error)
            try:
                rr = client.read_holding_registers(0,15,unit=UNIT)
                client.close()
                rospy.logwarn(rr.registers)
                rospy.logwarn("PLC-DASHGO working")
                robot.do_mission(rr.registers)
                rospy.sleep(1)
            except Exception as error:
                rospy.logwarn("Reading registers not ready")
                rospy.logwarn(error)   
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
