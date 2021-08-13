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

class Dashgo(object):
    # Create messages that are used to publish feedback/result
    _feedback = mobile_robot.msg.MobileRobotFeedback()
    _result = mobile_robot.msg.MobileRobotResult()

    def __init__(self, name):
        self._action_name = name
        rospy.loginfo(name)
        self.move_base_status = 0

        # Initialize move base client
        self.move_base_client = actionlib.SimpleActionClient('/' + self._action_name + '/move_base', MoveBaseAction)
        print("Waiting for move base client of " + self._action_name)
        self.move_base_client.wait_for_server()
        print(self._action_name + " running.")

        # Initialize Navigation Action Server
        self._as = actionlib.SimpleActionServer(self._action_name + "Server", MobileRobotAction, execute_cb=self.execute_cb, auto_start = False)
        self.moveBaseStatusTopic = rospy.Subscriber(self._action_name + "/move_base/status", GoalStatusArray, self.setServerFeedback)
        self.mobile_robot_request_pub = rospy.Publisher('/mobile_robot_requests', StaticRobotSignal, queue_size=10, latch=True)
        self._as.start()

        # Get context
        rospack = rospkg.RosPack()
        with open(os.path.join(rospack.get_path("contextualizer"), "contexts", "smart-factory.json"), 'r') as read_file:
            self.factory_context = json.load(read_file)
        print(self.factory_context)

        # Subscribe to calculate cost
        # rospy.Subscriber(self._action_name + "/move_base/DWAPlannerROS/global_plan", Path, publish_cost)

    # def publish_cost(self, path):
    #     prev_x = path.poses[0].pose.position.x
    #     prev_y = path.poses[0].pose.position.y
    #     cost = 0

    #     for pose in path.poses[1:]:
    #         cost+= math.sqrt(pow((pose.pose.position.x - prev_x),2)+ pow((pose.pose.position.y - prev_y),2))
    #         prev_x = pose.pose.position.x
    #         prev_y = pose.pose.position.y

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
            raw_pose = self.factory_context["static_robots"][process[0]]["output"][int(process[1])]
            point = Point()
            point.x = raw_pose[0]
            point.y = raw_pose[1]
            point.z = 0.0
            movebase_goal = MoveBaseGoal()
            movebase_goal.target_pose.header.frame_id = "/map"
            movebase_goal.target_pose.header.stamp = rospy.Time.now()
            movebase_goal.target_pose.pose = Pose(point,  Quaternion(raw_pose[2], raw_pose[3], raw_pose[4], raw_pose[5]))
            
            self.move_base_client.send_goal(movebase_goal)
            wait = self.move_base_client.wait_for_result()
            if not wait:
                rospy.loginfo("The robot failed to reach the destination")
                self._result.result = False
                self._as.set_aborted()
                return

            print("Robot " + self._action_name + " reached beginning!")
            # Publish output retrieved
            self.publish_request(process[0], 1)
            process = end.split("-")
            print("///////////////////////")
            print(process)

            raw_pose = self.factory_context["static_robots"][process[0]]["input"][int(process[1])]
            point = Point()
            point.x = raw_pose[0]
            point.y = raw_pose[1]
            point.z = 0.0
            movebase_goal = MoveBaseGoal()
            movebase_goal.target_pose.header.frame_id = "/map"
            movebase_goal.target_pose.header.stamp = rospy.Time.now()
            movebase_goal.target_pose.pose = Pose(point,  Quaternion(raw_pose[2], raw_pose[3], raw_pose[4], raw_pose[5]))
            
            self.move_base_client.send_goal(movebase_goal)
            wait = self.move_base_client.wait_for_result()
            if not wait:
                rospy.loginfo("The robot failed to reach the destination")
                self._result.result = "FAILED"
                self._as.set_aborted()
                return
            
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

    def setServerFeedback(self, data):
        if len(data.status_list):
            self.move_base_status = data.status_list[0].status

    def send_goal(self, goal_pose_given):
        rospy.loginfo(goal_pose_given)
        client = actionlib.SimpleActionClient(self._action_name + '/move_base', MoveBaseAction)
        client.wait_for_server()

        goal = goal_pose_given
        goal.target_pose.header.stamp = rospy.Time.now()
        client.send_goal(goal)
        while self.move_base_status != 1:
            print("Waiting for move_base to start")
            rospy.sleep(2)
        print("Move base status: " + str(self.move_base_status))
        # if (self.move_base_status not in [1, 0]):
        #     print("Error occured in movebase")
        #     return False
        rate = rospy.Rate(10.0)
        trans, rot = None, None
        distance = 1
        self.move_base_status = 1
        listener = tf.TransformListener()
        while self.move_base_status == 1:
            try:
                (trans,rot) = listener.lookupTransform('/map', self._action_name + '/base_link',rospy.Time(0))
                prev_trans = trans
                prev_rot = rot
                distance = math.sqrt(pow((goal.target_pose.pose.position.x - trans[0]),2)+ pow((goal.target_pose.pose.position.y - trans[1]),2))
                if distance < 0.3:
                    print("Close enough")
                    break
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue
        if distance > 0.3:
            print("Error occured in movebase")
            return False
        else:
            client.cancel_goal()
            print("Reached position.")
            return True


if __name__ == '__main__':
    rospy.sleep(1.)
    full_param_name = rospy.search_param('ns')
    ns = ""
    if rospy.get_param(full_param_name):
        ns = rospy.get_param(full_param_name)
        ns = ns["dashgo"]["ns"]
    rospy.loginfo("Initializing work station...")

    rospy.init_node(ns + '_dashgo', anonymous=True)
    server = Dashgo(ns)
    rospy.spin()