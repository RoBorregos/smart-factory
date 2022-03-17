#!/usr/bin/env python
import time
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32MultiArray as HoldingRegister
from nav_msgs.msg import Odometry
from std_msgs.msg import String, Int32


class Checkvel:
  def __init__(self):
    self.sub_imu = rospy.Subscriber('cmd_vel', Twist, self.imu_cb)
    self.velxlineal = 0
    self.velzangular = 0
    self.updatevelocity = 0
    self.batterypercentage = 100
    self.batterylos=1
    self.oldsecond = 0
    self.battery_status = rospy.Publisher("batterystatus",Int32 ,queue_size=10) 
  def main(self):
    rospy.sleep(0.3)
    newsecond= 0
    second = 0
    t = rospy.Time.from_sec(time.time())
    second = t.to_sec() 
    if self.velxlineal !=0 or self.velzangular !=0:
        newsecond = second - self.oldsecond
        if newsecond >=1:
            newsecond = 0
            #Update baterry
            #rospy.logwarn("time:"+str(self.batterypercentage))
            self.batterypercentage -= self.batterylos
            self.battery_status.publish(self.batterypercentage)
            self.oldsecond=second
    else:
        self.oldsecond=second

  def imu_cb(self, msg):
      self.velxlineal = msg.linear.x 
      self.velzangular = msg.angular.z



if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = Checkvel()
        r = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            robot.main()
            r.sleep()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
