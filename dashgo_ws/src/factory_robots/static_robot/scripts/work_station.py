#!/usr/bin/env python

import rospy
from std_msgs.msg import *
import actionlib
from static_robot.msg import *

'''
Internal states:
- initializing
- ready
- processing
- finished
- error

Possible actions:
- start_process
- restart
- cancel
'''

class WorkStation():
    # create messages that are used to publish feedback/result
    _feedback = static_robot.msg.StaticRobotFeedback()
    _result = static_robot.msg.StaticRobotResult()

    def __init__(self, name):
        self.state = "initializing"
        self._feedback.stateMachine = self.state
        self._as.publish_feedback(self._feedback)
        self._action_name = name + "_workstation"
        self._as = actionlib.SimpleActionServer(self._action_name, static_robot.msg.StaticRobot, execute_cb=self.execute_cb, auto_start = False)
        self.static_robot_request_pub = rospy.Publisher('/static_robot_requests', StaticRobotSignal, queue_size=10)
        self._as.start()
        
        rospy.loginfo("Workstation " + self._action_name[:12] + " ready for input.")
        # publishes request to FTM
        self.publish_request(False)

    def publish_request(self, io):
        workstation_request = StaticRobotSignal()
        # sends only id, without type
        workstation_request.id = self._action_name[:12]
        workstation_request.io = io
        self.static_robot_request_pub.publish(workstation_request)
        self.state = "ready" if io else "finished"
        self._feedback.stateMachine = self.state
        self._as.publish_feedback(self._feedback)


    def execute_cb(self, goal):
        if self.state = "error":
            rospy.loginfo("Work station " + self._action_name[:12] + " in error state.")
            self._as.set_rejected()
        elif goal.action == "start_process" and self.state == "ready":
            rospy.loginfo("Workstation " + self._action_name[:12] + " starting process.")
            self.state = "processing"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            rospy.sleep(5.)
            self.state = "finished"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            self._as.set_succeeded()
            self.publish_request(True)
        elif goal.action == "restart" and self.state == "finished":
            rospy.loginfo("Work station " + self._action_name[:12] + " ready for input.")
            self.publish_request(False)
            self._as.set_succeeded()
        elif goal.action == "cancel":
            rospy.loginfo("Work station " + self._action_name[:12] + " canceled.")
            self.state = "error"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            self._as.set_aborted()
        elif goal.action in ["start_process", "restart", "cancel"]:
            rospy.loginfo("Work station " + self._action_name[:12] + " cannot do action.")
            self._as.set_rejected()
        else:
            rospy.loginfo("Work station " + self._action_name[:12] + " received invalid action.")
            self._as.set_rejected()

if __name__ == '__main__':
    rospy.sleep(1.)
    full_param_name = rospy.search_param('ns')
    ns = ""
    if rospy.get_param(full_param_name):
        ns = rospy.get_param(full_param_name)
    rospy.loginfo("Initializing work station...")

    rospy.init_node(ns + '_work_station', anonymous=True)
    server = WorkStation(ns)
    rospy.spin()