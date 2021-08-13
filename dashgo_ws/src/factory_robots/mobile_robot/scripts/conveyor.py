#! /usr/bin/env python
from __future__ import print_function
import tf
import math
import os
import json

import actionlib
import rospy
import rospkg
from actionlib_msgs.msg import *
from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from mobile_robot.msg import *
from static_robot.msg import StaticRobotSignal

"""
Valid states:
    PENDING
    ACTIVE
    SUCCEEDED
    ABORTED
Valid Actions:
    - [#] -> process number
    - -1 -> cancel
"""

class Conveyor(object):
    # Create messages that are used to publish feedback/result
    _feedback = mobile_robot.msg.MobileRobotFeedback()
    _result = mobile_robot.msg.MobileRobotResult()

    def __init__(self, name):
        self._action_name = name
        rospy.loginfo(name)

        # Initialize Action Server
        self._as = actionlib.SimpleActionServer(self._action_name + "Server", MobileRobotAction, execute_cb=self.execute_cb, auto_start = False)
        self.mobile_robot_request_pub = rospy.Publisher('/mobile_robot_requests', StaticRobotSignal, queue_size=10, latch=True)
        self._as.start()

        # Get context
        rospack = rospkg.RosPack()
        with open(os.path.join(rospack.get_path("contextualizer"), "contexts", "smart-factory.json"), 'r') as read_file:
            self.factory_context = json.load(read_file)
        print(self.factory_context)

    def publish_request(self, id, io):
        storage_request = StaticRobotSignal()
        storage_request.id = id
        storage_request.io = io
        self.mobile_robot_request_pub.publish(storage_request)
    
    def execute_cb(self, goal):
        # Possible actions:
        # - [#] -> process number
        # - -1 -> cancel

        action = goal.process_step
        if action in range(len(self.factory_context["process_steps"])):
            beginning = self.factory_context["process_steps"][action][0]
            end = self.factory_context["process_steps"][action][1]
            
            process = beginning.split("-")
            print("///////////////////////")
            print(process)
            print("Robot " + self._action_name + " obtained input")
            rospy.sleep(5.)
            # Publish output retrieved
            self.publish_request(process[0], 1)
            process = end.split("-")
            print("///////////////////////")
            print(process)
            
            print("Robot " + self._action_name + " finished transportation.")
            # Publish input given
            self.publish_request(process[0], 0)

            self._result.result = "SUCCEDED"
            self._as.set_succeeded(self._result)
        elif action == -1:
            # TODO: Cancel actions and reset robot actuators
            self._as.set_aborted()
        else:
            self._as.se
            rospy.loginfo("Invalid Action")
            self._result = "FAILED"
            self._as.set_aborted()

if __name__ == '__main__':
    rospy.sleep(1.)
    full_param_name = rospy.search_param('ns')
    ns = ""
    if rospy.get_param(full_param_name):
        ns = rospy.get_param(full_param_name)
        ns = ns["conveyor"]["ns"]
    rospy.loginfo("Initializing work station...")

    rospy.init_node(ns + '_conveyor', anonymous=True)
    server = Conveyor(ns)
    rospy.spin()