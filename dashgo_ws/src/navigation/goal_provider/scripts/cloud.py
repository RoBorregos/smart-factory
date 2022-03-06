#!/usr/bin/env python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from firebase_admin import credentials
import time
import rospy
from std_msgs.msg import Int32,String

class Cloud:
  def __init__(self):
    cred = credentials.Certificate("google_services.json")
    firebase_admin.initialize_app(cred)
    self.db = firestore.client()
    self.battery_status = rospy.Subscriber("batterystatus", Int32, self.batterycallback)
    self.robot_status = rospy.Subscriber("robotstatus", String, self.robotcallback)
    self.mission_status = rospy.Publisher("missionstatus",String ,queue_size=10) 
    self.batterypercentage=100
    self.ro_status="Free"
  def robotcallback(self, msg):
      self.batterypercentage=msg.data
  def batterycallback(self, msg):
      self.ro_status=msg.data
  def main(self):
    rospy.sleep(1.)
    doc_ref = self.db.collection(u'Robots').document(u'DashgoB1')
    doc_ref.update({
        u'battery': self.batterypercentage,
        u'robotstatus': self.ro_status,
    })
    #Obtain info mission, send to robot
    mission="Nothing"
    snapshot = doc_ref.get()
    inforobot = snapshot.to_dict()
    mission=inforobot['mission']
    self.mission_status.publish(mission)





if __name__ == '__main__':
    try:
        rospy.init_node('Cloud_info')
        robot = Cloud()
        r = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rospy.logwarn("PLC-DASHGO Battery AI working")
            robot.main()
            r.sleep()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
