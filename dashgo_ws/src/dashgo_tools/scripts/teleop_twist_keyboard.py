#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import sys, select, termios, tty
from std_msgs.msg import Int32MultiArray as HoldingRegister

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >
t : up (+z)
b : down (-z)
anything else : stop
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
CTRL-C to quit

ModbusMode(0 OR 1):
a: Enable until is pressed again
b: Enable until is pressed again
d: Enable until is pressed again
f: Enable until is pressed again
g: Set mode (1)
h: Set mode (1)
v: Stop g and h (0)
"""

moveBindings = {
		'i':(1,0,0,0),
		'o':(1,0,0,-1),
		'j':(0,0,0,1),
		'l':(0,0,0,-1),
		'u':(1,0,0,1),
		',':(-1,0,0,0),
		'.':(-1,0,0,1),
		'm':(-1,0,0,-1),
		'O':(1,-1,0,0),
		'I':(1,0,0,0),
		'J':(0,1,0,0),
		'L':(0,-1,0,0),
		'U':(1,1,0,0),
		'<':(-1,0,0,0),
		'>':(-1,-1,0,0),
		'M':(-1,1,0,0),
		't':(0,0,1,0),
		'b':(0,0,-1,0),
	       }

speedBindings={
		'q':(1.1,1.1),
		'z':(.9,.9),
		'w':(1.1,1),
		'x':(.9,1),
		'e':(1,1.1),
		'c':(1,.9),
	      }
#location,value
#Se mantiene en uno hasta que se aplaste de nuevo: a,b,d,f
modbusmode = {
	"a": 0,
	"b": 0,
	"d": 0,
	"f": 0,
	"g": 0,
	"h": 0,
}

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

speed = 0.30
turn = 0.6
contadora = 0
contadorb = 0
contadord = 0
contadorf = 0
contadorg = 0
contadorh = 0
def vels(speed,turn):
	return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
	rospy.init_node('teleop_twist_keyboard')
	x = 0
	y = 0
	z = 0
	th = 0
	status = 0
	try:
		print msg
		print vels(speed,turn)
		while(1):
			key = getKey()
			rospy.logwarn(key)
			if key in moveBindings.keys():
				x = moveBindings[key][0]
				y = moveBindings[key][1]
				z = moveBindings[key][2]
				th = moveBindings[key][3]
			elif key in speedBindings.keys():
				speed = speed * speedBindings[key][0]
				turn = turn * speedBindings[key][1]
				print vels(speed,turn)
				if (status == 14):
					print msg
				status = (status + 1) % 15
			elif key in modbusmode.keys():
				contadora+=1 if key=="a" else contadora
				contadorb+=1 if key=="b" else contadorb
				contadord+=1 if key=="d" else contadord
				contadorf+=1 if key=="d" else contadorf
				if key=="a" and contadora<2:
					modbusmode[key]=1 
				elif key=="a" and contadora>=2:
					contadora=0
					modbusmode[key]=0 
				elif key=="b" and contadorb<2:
					modbusmode[key]=1 
				elif key=="b" and contadorb>=2:
					contadorb=0
					modbusmode[key]=0 
				elif key=="d" and contadord<2:
					modbusmode[key]=1 
				elif key=="d" and contadord>=2:
					contadord=0
					modbusmode[key]=0 
				elif key=="f" and contadorf<2:
					modbusmode[key]=1 
				elif key=="f" and contadorf>=2:
					contadorf=0
					modbusmode[key]=0 
				elif key=="g" and contadorg<2:
					modbusmode[key]=1 
				elif key=="g" and contadorg>=2:
					contadorg=0
					modbusmode[key]=0 
				elif key=="h" and contadorh<2:
					modbusmode[key]=1 
				elif key=="h" and contadorh>=2:
					contadorh=0
					modbusmode[key]=0 
				#Send info to modbusregister
				rospy.logwarn("Pressed"+key +" : " +str(modbusmode[key]))
				rospy.logwarn("a" +" : " +str(modbusmode["a"]))
				rospy.logwarn("b" +" : " +str(modbusmode["b"]))
				rospy.logwarn("d" +" : " +str(modbusmode["d"]))
				rospy.logwarn("f" +" : " +str(modbusmode["f"]))
				rospy.logwarn("g" +" : " +str(modbusmode["g"]))
				rospy.logwarn("h" +" : " +str(modbusmode["h"]))
				try:
				    client =  ModbusClient("192.168.31.2",port=502)
				    UNIT = 0x1
				    conexion = client.connect()
				    rospy.logwarn("Modbus connection ready")
				except Exception as error:
				    rospy.logwarn("Modbus connection error")
				    rospy.logwarn(error)
				try:
					outputregister = HoldingRegister()
					myregisters = list(modbusmode.values())
					outputregister.data = [int(i) for i in myregisters]
					rq = client.write_registers(10, outputregister.data, unit=UNIT)
					client.close()
					rospy.logwarn("PLC-DASHGO working")
					rospy.sleep(1)
				except Exception as error:
				    rospy.logwarn("Reading registers not ready")
				    rospy.logwarn(error)   
			else:
				x = 0
				y = 0
				z = 0
				th = 0
				if (key == '\x03'):
					break

			twist = Twist()
			twist.linear.x = x*speed; twist.linear.y = y*speed; twist.linear.z = z*speed;
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn
			pub.publish(twist)

	except Exception as error:
		print error

	finally:
		twist = Twist()
		twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
		twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		pub.publish(twist)

    	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
