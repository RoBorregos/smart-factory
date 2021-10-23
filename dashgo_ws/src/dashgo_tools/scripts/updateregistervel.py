#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from std_msgs.msg import Int32MultiArray as HoldingRegister




class Checkvel:
  def __init__(self):
    self.sub_imu = rospy.Subscriber('odom', Odometry, self.imu_cb)
    self.velxlineal = 0
    self.velzangular = 0
    self.updateregister = 0
    while not rospy.is_shutdown():
        rospy.sleep(0.3)
        rospy.loginfo("velxlineal:"+str((self.velxlineal)))
        rospy.loginfo("velxangular:"+str((self.velzangular)))
        self.updateregister =1 if self.velxlineal !=0 or self.velzangular !=0 else 0
        #Send info to modbusregister
        rospy.logwarn("Robot update register 16")
        try:
            client =  ModbusClient("192.168.31.2",port=502)
            UNIT = 0x1
            conexion = client.connect()
            rospy.logwarn("Modbus connection ready")
        except Exception as error:
            rospy.logwarn("Modbus connection error")
            rospy.logwarn(error)
        try:
            rq = client.write_registers(16,self.updateregister, unit=UNIT)
            client.close()
            rospy.logwarn("PLC-DASHGO working")
            rospy.sleep(1)
        except Exception as error:
            rospy.logwarn("Reading registers not ready")
            rospy.logwarn(error)   	


  def imu_cb(self, msg):
      self.velxlineal = msg.twist.twist.linear.x 
      self.velzangular = msg.twist.twist.linear.z

def main():
  rospy.init_node('updateregister')
  Checkvel()


if __name__ == '__main__':
  main()
