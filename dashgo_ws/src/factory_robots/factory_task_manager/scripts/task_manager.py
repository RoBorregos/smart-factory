#! /usr/bin/env python
from __future__ import print_function
import os
import json
import rospkg
import rospy
import actionlib
from static_robot.msg import *
from mobile_robot.msg import *

class TaskManager():

    def __init__(self):
        self.factory_context = None
        rospack = rospkg.RosPack()
        self.unassigned_action_stack = []
        self.assigned_action_stack = []
        with open(os.path.join(rospack.get_path("contextualizer"), "contexts", "smart-factory.json"), 'r') as read_file:
             self.factory_context = json.load(read_file)
        print("Context obtained.")

        # Robot action trigger subscribers
        print("Subscribing to triggers.")
        self.processState = []
        for _ in range(len(self.factory_context["process_steps"])):
            self.processState.append([False, False])
        rospy.Subscriber("/static_robot_requests", StaticRobotSignal, self.addIOTrigger)
        rospy.Subscriber("/mobile_robot_requests", StaticRobotSignal, self.addStaticRobotTrigger)

        # Action clients and services
        print("Connecting to robot action clients.")
        self.mobile_robot_clients = {}
        for mobile_robot_key in self.factory_context["mobile_robots"]:
            mobileRobotClient = actionlib.SimpleActionClient(mobile_robot_key + "/" + mobile_robot_key + 'Server', MobileRobotAction)
            self.mobile_robot_clients[mobile_robot_key] = mobileRobotClient
            print("Waiting for " + mobile_robot_key + "...", end='')
            self.mobile_robot_clients[mobile_robot_key].wait_for_server()
            print("done.")

        self.static_robot_clients = {}
        for static_robot_key in self.factory_context["static_robots"]:
            staticRobotClient = actionlib.SimpleActionClient(static_robot_key + "/" + static_robot_key + 'Server', StaticRobotAction)
            self.static_robot_clients[static_robot_key] = staticRobotClient
            print("Waiting for " + static_robot_key + "...", end='')
            self.static_robot_clients[static_robot_key].wait_for_server()
            print("done.")

        self.process_history = []

    def addIOTrigger(self, action_msg):
        io = (action_msg.io+1)%2
        for index, process in enumerate(self.factory_context["process_steps"]):
            if process[io] == action_msg.id:
                self.processState[index][io] = True
                if self.processState[index] == [True, True]:
                    self.addToActionStack(index)
                    self.processState[index] = [False, False]
                    print("Process ready, added to action stack.")
                break
        # print(self.processState)
        # print("Received IO ready/retrieved trigger.")

    def addStaticRobotTrigger(self, msg):
        # id - static_robot-#
        # io - bool
        data = msg.id.split("-")
        static_robot_type = self.factory_context["static_robots"][data[0]]["type"]
        goal = StaticRobotGoal()
        if  static_robot_type == "workstation":
            goal.action = "restart" if msg.io else "start_process"
        elif static_robot_type == "storage":
            goal.action = "restock" if msg.io else "store"
        self.static_robot_clients[data[0]].send_goal(goal)
        print("Received static robot trigger.")


    def addToActionStack(self, process_index):
        # TODO: Add to action queue according to priority
        self.unassigned_action_stack.append(process_index)
        self.unassigned_action_stack = sorted(self.unassigned_action_stack)[::-1]
        print(self.unassigned_action_stack)
        for processtate in self.processState:
            print(processtate)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    def delegate_actions(self):
        # for action in self.unassigned_action_stack:
        #     print(action)
        # # for processtate in self.processState:
        # #     print(processtate)
        for action in self.unassigned_action_stack:
            for mobile_robot in self.mobile_robot_clients:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(self.factory_context["mobile_robots"][mobile_robot]["type"] + " " + self.factory_context["process_steps"][action][-1])
                print(self.factory_context["mobile_robots"][mobile_robot]["type"] == self.factory_context["process_steps"][action][-1])
                if self.mobile_robot_clients[mobile_robot].get_state() in [2, 3, 8, 9] and self.factory_context["mobile_robots"][mobile_robot]["type"] == self.factory_context["process_steps"][action][-1]:
                    # See http://docs.ros.org/en/kinetic/api/actionlib_msgs/html/msg/GoalStatus.html
                    goal = MobileRobotGoal()
                    self.process_history.append(self.unassigned_action_stack.pop())
                    goal.process_step = self.process_history[-1]
                    self.mobile_robot_clients[mobile_robot].send_goal(goal)
                    break


if __name__ == '__main__':
    try:
        rospy.init_node('task_makager')
        taskManager = TaskManager()
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            taskManager.delegate_actions()
            rate.sleep()
        rospy.spin()
            
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)