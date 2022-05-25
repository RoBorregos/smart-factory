#!/usr/bin/env python2
import time
import rospy
from std_msgs.msg import Int32,String
from nav_msgs.msg import Path
from geometry_msgs.msg import Vector3
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from std_msgs.msg import Int32MultiArray as HoldingRegister
import math
class Server:
  def __init__(self):
    self.battery_status = rospy.Subscriber("batterystatus", Int32, self.batterycallback)
    self.robot_status = rospy.Subscriber("robotstatus", String, self.robotcallback)
    self.newgoal =  rospy.Publisher("newcoordiantes",Vector3 ,queue_size=10) 
    self.mission_status = rospy.Publisher("missionstatus",Int32 ,queue_size=10) 
    self.plan_distance = rospy.Subscriber("path_test_server", Path, self.distance_callback)
    self.batterypercentage=100
    self.ro_status="Free"
    self.status=2
    self.outputregister = HoldingRegister()
    self.statusoptions = {"Charging":0,"Moving":1,"Free":2, "Success":3,"Failure":4}
    #Registers: RobotStatus, Goalx, Goaly, Battery, MissionStatus, Distance,
    self.modbusmode = {
	"Battery": 0,   #0-100
	"RobotStatus": 0,    #0-Charging, 1-Moving, 2-Free
	"Distance": 0,
    }
    self.distancegoal= 0.0
  def batterycallback(self, msg):
      self.batterypercentage=msg.data
  def robotcallback(self, msg):
      self.ro_status=msg.data
  def distance_callback(self,data):
      if self.status==1: #Move
          for i in range(len(data.poses)-1):
              self.distancegoal += math.sqrt(pow((data.poses[i+1].pose.position.x - data.poses[i].pose.position.x),2) + pow((data.poses[i+1].pose.position.y - data.poses[i].pose.position.y), 2))
          rospy.loginfo("INFO DISTANCIAAAAAA")
          rospy.loginfo(self.distancegoal)

if __name__ == '__main__':
    try:
        rospy.init_node('Server_info')
        robot = Server()
        r = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            try:
                client =  ModbusClient("10.22.231.39",port=12345) #Server second computer
                UNIT = 0x1
                conexion = client.connect()
                rospy.logwarn("Modbus connection ready")
            except Exception as error:
                rospy.logwarn("Modbus connection error")
                rospy.logwarn(error)
            try:
                rr = client.read_holding_registers(0,15,unit=UNIT)
                rospy.logwarn(rr.registers)
                rospy.logwarn("Info robot working")
                robot.status = rr.registers[0] #MissionStatus 0-Charge, 1-Move, 2-Free, 3-Success, 4-Failure
                goalx = rr.registers[1]/1000.0  #Goalx
                goaly = rr.registers[2]/1000.0  #Goaly
                robot.mission_status.publish(robot.status)
                #Send info to planner trayectory to receive distance
                robot.newgoal.publish(Vector3(goalx,goaly,0.0))

                robot.modbusmode["Battery"] = robot.batterypercentage
                robot.modbusmode["RobotStatus"] = robot.statusoptions[robot.ro_status]
                robot.modbusmode["Distance"] = robot.distancegoal*1000
                myregisters = list(robot.modbusmode.values())
                robot.outputregister.data = [int(i) for i in myregisters]
                rq = client.write_registers(4, robot.outputregister.data, unit=UNIT)     
                client.close()
                rospy.sleep(1)
            except Exception as error:
                rospy.logwarn("Reading registers not ready")
                rospy.logwarn(error)  
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
