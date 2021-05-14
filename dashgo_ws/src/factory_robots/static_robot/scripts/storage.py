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
- error

Possible actions:
- store
- restock
- cancel
'''

class Storage():
    # create messages that are used to publish feedback/result
    _feedback = static_robot.msg.StaticRobotFeedback()
    _result = static_robot.msg.StaticRobotResult()

    def __init__(self, name):
        self.state = "initializing"
        self._feedback.stateMachine = self.state
        self._as.publish_feedback(self._feedback)
        self._action_name = name + "_storage"
        self._as = actionlib.SimpleActionServer(self._action_name, static_robot.msg.StaticRobot, execute_cb=self.execute_cb, auto_start = False)
        self.static_robot_request_pub = rospy.Publisher('/static_robot_requests', StaticRobotSignal, queue_size=10)
        self._as.start()
        
        rospy.loginfo("Storage " + self._action_name[:8] + " ready for input.")
        # publishes request to FTM
        self.publish_request(False)

    def publish_request(self, io):
        storage_request = StaticRobotSignal()
        # sends only id, without type
        storage_request.id = self._action_name[:8]
        storage_request.io = io
        self.static_robot_request_pub.publish(storage_request)
        self.state = "ready"
        self._feedback.stateMachine = self.state
        self._as.publish_feedback(self._feedback)


    def execute_cb(self, goal):
        # TODO: Call the corresponding actions servers for storing input 
        # and retrieving output to validate goal
        if self.state = "error":
            rospy.loginfo("Storage " + self._action_name[:8] + " in ERROR state.")
            self._result.result = "error"
            self._as.set_rejected(self._result)
        elif goal.action == "store" and self.state == "ready":
            rospy.loginfo("Storage " + self._action_name[:8] + " starting storing process.")
            self.state = "processing"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            rospy.sleep(5.)
            self._result.result = "stored"
            self._as.set_succeeded(self._result)
            self.publish_request(False)
        elif goal.action == "restock" and self.state == "ready":
            rospy.loginfo("Storage " + self._action_name[:8] + " starting retrieval.")
            self.state = "processing"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            rospy.sleep(5.)
            self._result.result = "stored"
            self._as.set_succeeded(self._result)
            self.publish_request(True)
        elif goal.action == "cancel":
            rospy.loginfo("Storage " + self._action_name[:8] + " canceled.")
            self.state = "error"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            self._result.result = "canceled"
            self._as.set_aborted(self._result)
        elif goal.action in ["store", "restock", "cancel"]:
            rospy.loginfo("Storage " + self._action_name[:8] + " cannot do action right now.")
            self._result.result = "busy"
            self._as.set_rejected(self._result)
        else:
            rospy.loginfo("Storage " + self._action_name[:8] + " received invalid action.")
            self._result.result = "invalid"
            self._as.set_rejected(self._result)

if __name__ == '__main__':
    rospy.sleep(1.)
    full_param_name = rospy.search_param('ns')
    ns = ""
    if rospy.get_param(full_param_name):
        ns = rospy.get_param(full_param_name)
    rospy.loginfo("Initializing storage...")

    rospy.init_node(ns + '_storage', anonymous=True)
    server = Storage(ns)
    rospy.spin()