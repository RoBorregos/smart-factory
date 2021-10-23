#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from std_msgs.msg import Int32MultiArray as HoldingRegister

update1 = 0

if __name__=="__main__":
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	rospy.init_node('updateregister')
	x = 0
	y = 0
	z = 0
	th = 0
	status = 0
	try:
        twist = Twist()
        twist.linear.x = x*speed; twist.linear.y = y*speed; twist.linear.z = z*speed;
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn
        pub.publish(twist)

        if twist.linear.x != 0:
            #Send info to modbusregister
            rospy.logwarn("Robot moving update register 16")
            try:
                client =  ModbusClient("192.168.31.2",port=502)
                UNIT = 0x1
                conexion = client.connect()
                rospy.logwarn("Modbus connection ready")
            except Exception as error:
                rospy.logwarn("Modbus connection error")
                rospy.logwarn(error)
            try:
                rq = client.write_registers(16,1, unit=UNIT)
                client.close()
                rospy.logwarn("PLC-DASHGO working")
                rospy.sleep(1)
            except Exception as error:
                rospy.logwarn("Reading registers not ready")
                rospy.logwarn(error)   
        else:
            #Send info to modbusregister
            rospy.logwarn("Robot not moving update register 16")
            try:
                client =  ModbusClient("192.168.31.2",port=502)
                UNIT = 0x1
                conexion = client.connect()
                rospy.logwarn("Modbus connection ready")
            except Exception as error:
                rospy.logwarn("Modbus connection error")
                rospy.logwarn(error)
            try:
                rq = client.write_registers(16,0, unit=UNIT)
                client.close()
                rospy.logwarn("PLC-DASHGO working")
                rospy.sleep(1)
            except Exception as error:
                rospy.logwarn("Reading registers not ready")
                rospy.logwarn(error)   				

