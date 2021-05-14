#! /usr/bin/env python
from __future__ import print_function
import tf
import math

import actionlib
import rospy
from actionlib_msgs.msg import *
from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import mobile_robot.msg

"""
Valid states:
    PENDING
    ACTIVE
    SUCCEEDED
    ABORTED
Valid Actions:
    - transport_to
    - cancel
"""

class Dashgo(object):
    # Create messages that are used to publish feedback/result
    _feedback = mobile_robot.msg.MobileRobotFeedback()
    _result = mobile_robot.msg.MobileRobotResult()

    def __init__(self, name):
        self._action_name = name
        rospy.loginfo(name)
        self.move_base_status = 0
        self.pub_amcl = rospy.Publisher('initialpose', PoseWithCovarianceStamped, queue_size=10)
        # Initialize Navigation Action Server
        self._as = actionlib.SimpleActionServer(self._action_name + "Server", mobile_robot.msg.MobileRobotAction, execute_cb=self.execute_cb, auto_start = False)
        self.moveBaseStatusTopic = rospy.Subscriber(self._action_name + "/move_base/status", GoalStatusArray, self.setServerFeedback)
        self._as.start()
        with open("./src/contextualizer/context/smart-factory.json", "r") as read_file:
            self.factory_context = json.load(read_file)
        print(self.factory_context)
    
    def execute_cb(self, goal):
        # Possible actions:
        # - transport_to
        # - cancel

        action = goal.process_step

        if action in []:
            pose = goal.pose
            actionResult = self.send_goal(pose)
            if not actionResult:
                rospy.loginfo("The robot failed to reach the destination")
                self._result.result = False
                self._as.set_aborted()
                return
            print("Robot reached destination!")
            self._result = True
            self._as.set_succeeded()
        elif action == "cancel":
            # TODO: Cancel actions and reset robot actuators
            rospy.loginfo("Executing teleop action")
            currentAction = moveBase()
            currentAction.cancelGoal()
            self._as.set_aborted(self._result)
        else:
            self._as.se
            rospy.loginfo("Invalid Action")
            self._result = False
            self._as.set_rejected()

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
    rospy.loginfo("Initializing work station...")

    rospy.init_node(ns + '_dashgo', anonymous=True)
    server = Dashgo(ns)
    rospy.spin()