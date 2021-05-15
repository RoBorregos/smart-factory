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
        self._input_counter = 0
        self._feedback.stateMachine = self.state
        self._as.publish_feedback(self._feedback)
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name + "WorkstationServer", static_robot.msg.StaticRobot, execute_cb=self.execute_cb, auto_start = False)
        self.static_robot_request_pub = rospy.Publisher('/static_robot_requests', StaticRobotSignal, queue_size=10)
        self._as.start()
        self.state = "ready"
        self.workstation_context = None
        with open("./src/navigation/contextualizer/contexts/smart-factory.json", "r") as read_file:
             self.workstation_context = json.load(read_file)
        self.workstation_context =  self.workstation_context["static_robots"][self._action_name]
        rospy.loginfo("Workstation " + self._action_name + " ready for input.")
        print(self.workstation_context)
        # publishes request to FTM
        self.publish_request(False)

    def publish_request(self, io):
        workstation_request = StaticRobotSignal()
        workstation_request.io = io
        context_io = "output" if io else "input"
        for index, _ in enumerate(context[context_io]):
            workstation_request.id = self._action_name + "_" + index
            self.static_robot_request_pub.publish(workstation_request)
        self.state = "ready" if io else "finished"
        self._feedback.stateMachine = self.state
        self._as.publish_feedback(self._feedback)


    def execute_cb(self, goal):
        if self.state = "error":
            rospy.loginfo("Work station " + self._action_name + " in error state.")
            self._as.set_rejected()
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
                self._as.set_succeeded()
                self.publish_request(True)
        elif goal.action == "restart" and self.state == "finished":
            rospy.loginfo("Work station " + self._action_name + " ready for input.")
            self.publish_request(False)
            self._as.set_succeeded()
        elif goal.action == "cancel":
            rospy.loginfo("Work station " + self._action_name + " canceled.")
            self.state = "error"
            self._feedback.stateMachine = self.state
            self._as.publish_feedback(self._feedback)
            self._as.set_aborted()
        elif goal.action in ["start_process", "restart", "cancel"]:
            rospy.loginfo("Work station " + self._action_name + " cannot do action.")
            self._as.set_rejected()
        else:
            rospy.loginfo("Work station " + self._action_name + " received invalid action.")
            self._as.set_rejected()

if __name__ == '__main__':
    rospy.sleep(1.)
    namespace = rospy.search_param('ns')
    ns = ""
    if rospy.get_param(namespace):
        ns = rospy.get_param(namespace)
    
    rospy.loginfo("Initializing work station...")

    rospy.init_node(ns + '_workstation', anonymous=True)
    server = WorkStation(ns)
    rospy.spin()