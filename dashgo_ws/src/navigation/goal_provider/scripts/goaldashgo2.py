#!/usr/bin/env python2
import time
import rospy
import tf
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray as HoldingRegister
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
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.oldcoordinatex = 0.0
        self.oldcoordinatey = 0.0
        self.oldcoordinatez = 0.0
        self.cont=0
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
        modbusbase = plcregisters[7]
        initregisters = plcregisters[8]
        modbusregisters = HoldingRegister()
        newlist = [0]*10
        if (modbusbase != 0  and initregisters !=0):
            initregisters_list = [int(a) for a in str(initregisters)]
            for i in initregisters_list:
                newlist[i] = 1
            modbusregisters.data = newlist
        if(plcregisters[0]== 0 and plcregisters[1] !=0 and plcregisters[2]!=0):
            rospy.logwarn("Manual mode ready")
            angle = plcregisters[3] * math.pi/180
            ax =  float(plcregisters[1])/1000
            ay =  float(plcregisters[2])/1000
            a = [ ax, ay,0.000,0.000,0.000,0.000,0.000] #Ax,Ay,Az,qx,qy,qz,qw
            a[3] = 0.000
            a[4] = 0.000
            a[5] = math.sin(angle/2)
            a[6] = math.cos(angle/2)
            self.send_infomodbus(9,1) #Update Status occupied
            newcoordinatex = plcregisters[4]
            newcoordinatey =plcregisters[5]
            newcoordinatez = plcregisters[6]
            status = self.sendGoal1(a)
            if (status):
                if(self.oldcoordinatex !=newcoordinatex or self.oldcoordinatey !=newcoordinatey or self.oldcoordinatez !=newcoordinatez ):
                    if self.cont ==1:
                        self.send_infomodbus(9,2) #Update Status success
                        rospy.sleep(5)
                        self.cont=2
                    self.send_infomodbus(9,0) #Update Status success
            else:
                if(self.oldcoordinatex !=newcoordinatex or self.oldcoordinatey !=newcoordinatey or  self.oldcoordinatez !=newcoordinatez ):
                    self.send_infomodbus(9,1) #Update Status occupied
                    self.cont =1
            socket_pub.publish("arrive")
            self.oldcoordinatex = newcoordinatex
            self.oldcoordinatey = newcoordinatey
            self.oldcoordinatez = newcoordinatez
        elif(plcregisters[0]== 1 and plcregisters[4] !=0 and plcregisters[5]!=0):
            rospy.logwarn("Auto mode ready")
            angle = plcregisters[6] * math.pi/180
            ax = float(plcregisters[4])/1000
            ay = float(plcregisters[5])/1000 
            a = [ ax, ay,0.000,0.000,0.000,0.000,0.000] #Ax,Ay,Az,qx,qy,qz,qw
            a[3] = 0.000
            a[4] = 0.000
            a[5] = math.sin(angle/2)
            a[6] = math.cos(angle/2)
            newcoordinatex = plcregisters[4]
            newcoordinatey =plcregisters[5]
            newcoordinatez = plcregisters[6]
            if(self.oldcoordinatex !=newcoordinatex or self.oldcoordinatey !=newcoordinatey or  self.oldcoordinatez !=newcoordinatez ):
                self.send_infomodbus(9,1) #Update Status occupied
            self.sendGoal1(a)
            status = self.sendGoal1(a)
            if (status):
                if(self.oldcoordinatex !=newcoordinatex or self.oldcoordinatey !=newcoordinatey or self.oldcoordinatez !=newcoordinatez ):
                    self.send_infomodbus(9,2) #Update Status success
                    rospy.sleep(5)
                    self.send_infomodbus(9,0) #Update Status success
            socket_pub.publish("arrive")
            self.oldcoordinatex = newcoordinatex
            self.oldcoordinatey = newcoordinatey
            self.oldcoordinatez = newcoordinatez
        elif(plcregisters[0]== 2):
            rospy.logwarn("Stop mode ready")
    def test(self, index):
        socket_pub = rospy.Publisher("navBridgeServer/talker", String) 
        rospy.Subscriber("move_base/status", GoalStatusArray, self.setServerFeedback)
        a = goal_path[index]
        self.sendGoal1(a)
        socket_pub.publish("arrive")
        if index ==0:
            rospy.logwarn("Turn on 10-11,12")
            self.send_infomodbus(10,1)
            self.send_infomodbus(11,1)
            self.send_infomodbus(12,1)
            rospy.sleep(5)
            rospy.logwarn("Turn off 10-11,12")
            self.send_infomodbus(10,0)
            self.send_infomodbus(11,0)
            self.send_infomodbus(12,0)
    def send_infomodbus(self,index,value):
        try:
            client =  ModbusClient("192.168.31.2",port=502)
            UNIT = 0x1
            conexion = client.connect()
        except Exception as error:
            rospy.logwarn(error)
        try:
            rq = client.write_registers(index,value, unit=UNIT)
            client.close()
            rospy.logwarn("Infomodbus working")
            rospy.sleep(1)
        except Exception as error:
            rospy.logwarn("Infomodbus not ready")
            rospy.logwarn(error)      
    def send_infomodbus_list(self,index,modbusregisters):
        try:
            client =  ModbusClient("192.168.31.2",port=502)
            UNIT = 0x1
            conexion = client.connect()
        except Exception as error:
            rospy.logwarn(error)
        try:
            rq = client.write_registers(index,modbusregisters.data, unit=UNIT)
            client.close()
            rospy.logwarn("Infomodbus_list working")
            rospy.sleep(1)
        except Exception as error:
            rospy.logwarn("Infomodbus_list not ready")
            rospy.logwarn(error) 
        
if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        robot.send_infomodbus(9,0)
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
                rospy.loginfo("PLC Registers:")
                rospy.logwarn(rr.registers)
                rospy.logwarn("PLC-DASHGO2 working")
                robot.do_mission(rr.registers)
                rospy.sleep(1)
            except Exception as error:
                rospy.logwarn("Reading registers not ready")
                rospy.logwarn(error)   
            # try:
            #     rospy.logwarn("Turn on 10-11,12")
            #     robot.send_infomodbus(10,1)
            #     robot.send_infomodbus(11,1)
            #     rospy.sleep(5)
            #     rospy.logwarn("Turn off 10-11,12")
            #     robot.send_infomodbus(10,0)
            #     robot.send_infomodbus(11,0)
            #     for i in range(len(goal_path)):
            #         robot.test(i)
            # except Exception as error:
            #     rospy.logwarn(error)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
