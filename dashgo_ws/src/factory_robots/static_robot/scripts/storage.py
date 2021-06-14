#!/usr/bin/env python

import rospy
from std_msgs.msg import *
import actionlib
from static_robot.msg import *
import os
import json
import rospkg

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
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name + "Server", StaticRobotAction, execute_cb=self.execute_cb, auto_start = False)
        self.static_robot_request_pub = rospy.Publisher('/static_robot_requests', StaticRobotSignal, queue_size=10, latch=True)
        self._as.start()

        rospack = rospkg.RosPack()
        with open(os.path.join(rospack.get_path("contextualizer"), "contexts", "smart-factory.json"), 'r') as read_file:
             self.storage_context = json.load(read_file)
        self.storage_context =  self.storage_context["static_robots"][self._action_name]
        
        rospy.loginfo("Storage " + self._action_name + " ready for input.")
        # publishes request to FTM
        self.publish_request(False)
        rospy.sleep(0.1)
        self.publish_request(True)

    def publish_request(self, io):
        storage_request = StaticRobotSignal()
        io_list = "input" if io == False else "output"
        for index, _ in enumerate(self.storage_context[io_list]):
            storage_request.id = self._action_name + "-" + str(index)
            storage_request.io = io
            self.static_robot_request_pub.publish(storage_request)
            print("I've sent a static_robot_request")
            rospy.sleep(0.1)
        self.state = "ready"
        self._feedback.stateMachine = self.state


    def execute_cb(self, goal):
        # TODO: Call the corresponding actions servers for storing input 
        # and retrieving output to validate goal
        if self.state == "error":
            rospy.loginfo("Storage " + self._action_name + " in ERROR state.")
            self._result.result = "error"
            self._as.set_rejected(self._result)
        elif goal.action == "store" and self.state == "ready":
            rospy.loginfo("Storage " + self._action_name + " starting storing process.")
            self.state = "processing"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            rospy.sleep(5.)
            self._result.result = "stored"
            self._as.set_succeeded(self._result)
            self.publish_request(False)
            self._as.publish_feedback(self._feedback)
        elif goal.action == "restock" and self.state == "ready":
            rospy.loginfo("Storage " + self._action_name + " starting retrieval.")
            self.state = "processing"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            rospy.sleep(5.)
            self._result.result = "stored"
            self._as.set_succeeded(self._result)
            self.publish_request(True)
            self._as.publish_feedback(self._feedback)
        elif goal.action == "cancel":
            rospy.loginfo("Storage " + self._action_name + " canceled.")
            self.state = "error"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            self._result.result = "canceled"
            self._as.set_aborted(self._result)
        elif goal.action in ["store", "restock", "cancel"]:
            rospy.loginfo("Storage " + self._action_name + " cannot do action right now.")
            self._result.result = "busy"
            self._as.set_rejected(self._result)
        else:
            rospy.loginfo("Storage " + self._action_name + " received invalid action.")
            self._result.result = "invalid"
            self._as.set_rejected(self._result)

if __name__ == '__main__':
    rospy.sleep(1.)
    full_param_name = rospy.search_param('ns')
    ns = ""
    if rospy.get_param(full_param_name):
        ns = rospy.get_param(full_param_name)
        ns = ns["storage"]["ns"]
    rospy.loginfo("Initializing storage...")

    rospy.init_node(ns + '_storage', anonymous=True)
    server = Storage(ns)
    rospy.spin()