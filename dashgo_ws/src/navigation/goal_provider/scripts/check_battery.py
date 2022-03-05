#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from std_msgs.msg import Int32MultiArray as HoldingRegister
from nav_msgs.msg import Odometry
from std_msgs.msg import String, Float32


class Checkvel:
  def __init__(self):
    self.sub_imu = rospy.Subscriber('odom', Odometry, self.imu_cb)
    self.velxlineal = 0
    self.velzangular = 0
    self.updatevelocity = 0
    self.batterypercentage = 100
    self.batterylos=-2
    self.oldsecond = 0
    self.battery_status = rospy.Publisher("batterystatus",Int32 ) 
  def main(self):
    rospy.sleep(0.3)
    rospy.loginfo("velxlineal:"+str((self.velxlineal)))
    rospy.loginfo("velzangular:"+str((self.velzangular)))
    newsecond= 0
    second = 0
    t = rospy.Time.from_sec(time.time())
    second = t.to_sec() 
    if self.velxlineal !=0 or self.velzangular !=0:
        newsecond = second - self.oldsecond
        if newsecond >=1:
            newsecond = 0
            #Update baterry
            self.batterypercentage -= self.batterylos
            self.battery_status.publish(self.batterypercentage)
        else:
            self.oldsecond=second
    else:
        self.oldsecond=second
        self.updatevelocity= 0

  def imu_cb(self, msg):
      self.velxlineal = msg.twist.twist.linear.x 
      self.velzangular = msg.twist.twist.angular.z

def main():
  rospy.init_node('updatevelocity')
  Checkvel()


if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = Checkvel()
        r = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rospy.logwarn("PLC-DASHGO Battery AI working")
            robot.main()
            r.sleep()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
