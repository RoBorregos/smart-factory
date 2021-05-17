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
        with open(os.path.join(rospack.get_path("contextualizer"), "contexts", "smart-factory.json"), 'r') as read_file:
             self.factory_context = json.load(read_file)
        
        # Action clients and services
        self.mobile_robot_clients = []
        for mobile_robot in self.factory_context["mobile_robots"]:
            mobileRobotClient = actionlib.SimpleActionClient(mobile_robot["id"] + 'Server', MobileRobotAction)
            self.mobile_robot_clients.append(mobileRobotClient)

        self.static_robot_clients = {}
        for static_robot_key in self.factory_context["static_robots"]:
            staticRobotClient = actionlib.SimpleActionClient(mobile_robot["id"] + 'Server', StaticRobotAction)
            self.static_robot_clients[static_robot_key] = staticRobotClient

        self.unassigned_action_stack = []
        self.assigned_action_stack = []

        self.processState = []
        for _ in range(len(self.factory_context["process_steps"])):
            self.processState.append([False, False])

    def addIOTrigger(self, action_msg):
        io = action_msg.io
        for index, process in enumerate(self.factory_context["process_steps"]):
            if process[io] == action_msg.id:
                self.processState[index][io] = True
                if self.processState[index] == [True, True]:
                    self.addToActionStack(index)
                    self.processState[index] = [False, False]
                break
        print(self.processState)

    def addStaticRobotTrigger(self, msg):
        # static_robot-#
        # io
        data = msg.split("-")
        static_robot_type = self.factory_context["static_robots"][data[0]]["type"]
        if  static_robot_type == "workstation":
            goal = actions.msg.navServGoal(action = "restart" if io else "start_process")
        elif static_robot_type == "storage":
            goal = actions.msg.navServGoal(action = "restock" if io else "store")
        self.static_robot_clients[data[0]].send_goal(goal)


    def addToActionStack(self, process_index):
        # TODO: Add to action queue according to priority
        self.unassigned_action_stack.append(index)


    def delegate_actions(self):
        for action in self.unassigned_action_stack:
            print(action)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# def navigationClient():
#     # Creates the SimpleActionClient, passing the type of the action
#     # (NavigationAction) to the constructor.

#     # Waits until the action server has started up and started
#     # listening for goals.
#     client.wait_for_server()
#     print("Dashgo server running...")

#     # Creates a goal to send to the action server.
#     goal = actions.msg.navServGoal(process_step = 0)

#     # Sends the goal to the action server.
#     client.send_goal(goal)

#     # Waits for the server to finish performing the action.
#     client.wait_for_result()

#     # Prints out the result of executing the action
#     return client.get_result()  # The Navigation status result


if __name__ == '__main__':
    try:
        rospy.init_node('task_makager')
        taskManager = TaskManager()
        # Robot action triggers
        rospy.Subscriber("static_robot_requests", StaticRobotSignal, taskManager.addIOTrigger)
        rospy.Subscriber("mobile_robot_requests", StaticRobotSignal, taskManager.addStaticRobotTrigger)

        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            taskManager.delegate_actions()
            rate.sleep()
        rospy.spin()
            
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)