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
- finished
- error

Possible actions:
- start_process
- restart
- cancel
'''

class WorkStation():
    # create messages that are used to publish feedback/result
    _feedback = StaticRobotFeedback()
    _result = StaticRobotResult()

    def __init__(self, name):
        self.state = "initializing"
        self._action_name = name
        self._input_counter = 0
        self._feedback.stateMachine = self.state
        self._as = actionlib.SimpleActionServer(self._action_name + "Server", StaticRobotAction, execute_cb=self.execute_cb, auto_start = False)
        self.static_robot_request_pub = rospy.Publisher('/static_robot_requests', StaticRobotSignal, queue_size=10, latch=True)
        self._as.start()
        self.state = "ready"
        self.workstation_context = None
        rospack = rospkg.RosPack()
        with open(os.path.join(rospack.get_path("contextualizer"), "contexts", "smart-factory.json"), 'r') as read_file:
             self.workstation_context = json.load(read_file)
        self.workstation_context =  self.workstation_context["static_robots"][self._action_name]
        rospy.loginfo("Workstation " + self._action_name + " ready for input.")
        print(self.workstation_context)
        # publishes request to FTM to get input
        self.publish_request(False)

    def publish_request(self, io):
        workstation_request = StaticRobotSignal()
        workstation_request.io = io
        context_io = "output" if io else "input"
        for index, _ in enumerate(self.workstation_context[context_io]):
            workstation_request.id = self._action_name + "-" + str(index)
            self.static_robot_request_pub.publish(workstation_request)
            print(workstation_request.id)
            rospy.sleep(0.1)
        # self.state = "finished" if io else "ready"
        self._feedback.stateMachine = self.state


    def execute_cb(self, goal):
        if self.state == "error":
            rospy.loginfo("Work station " + self._action_name + " in error state.")
            self._as.set_aborted()
        elif goal.action == "start_process" and self.state == "ready":
            self._input_counter+=1
            if self._input_counter == len(self.workstation_context["input"]):
                self._input_counter = 0
                rospy.loginfo("Workstation " + self._action_name + " starting process.")
                self.state = "processing"
                self._feedback.stateMachine = self.state
                self._as.publish_feedback(self._feedback)
                rospy.sleep(5.)
                self.state = "finished"
                self._feedback.stateMachine = self.state
                self._as.publish_feedback(self._feedback)
                self.publish_request(True)
                self._as.publish_feedback(self._feedback)
                self._as.set_succeeded()
        elif goal.action == "restart" and self.state == "finished":
            self.state = "ready"
            rospy.loginfo("Work station " + self._action_name + " ready for input.")
            self.publish_request(False)
            self._as.publish_feedback(self._feedback)
            self._as.set_succeeded()
        elif goal.action == "cancel":
            rospy.loginfo("Work station " + self._action_name + " canceled.")
            self.state = "error"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            self._as.set_aborted()
        elif goal.action in ["start_process", "restart", "cancel"]:
            rospy.loginfo("Work station " + self._action_name + " cannot do action.")
            self._as.set_aborted()
        else:
            rospy.loginfo("Work station " + self._action_name + " received invalid action.")
            self._as.set_aborted()

if __name__ == '__main__':
    rospy.sleep(1.)
    namespace = rospy.search_param('ns')
    ns = ""
    if rospy.get_param(namespace):
        ns = rospy.get_param(namespace)
        ns = ns["work_station"]["ns"]
    rospy.loginfo("Initializing work station...")

    rospy.init_node(ns + '_workstation', anonymous=True)
    server = WorkStation(ns)
    rospy.spin()