#!/usr/bin/env python
import sys
import random

import rospy
import actionlib

from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from task_allocation.msg import TaskBid, FactoryTask

# goal = MoveBaseGoal()
# goal.target_pose.pose = Pose(Point(1.5, -4.85, 0), Quaternion(0.0, 0.0, 0.6, 0.77))
# goal.target_pose.header.frame_id = "map" 
# goal.target_pose.header.stamp = rospy.Time() 
# self.sac.send_goal(goal, active_cb=self.active_callback, done_cb=self.done_callback, feedback_cb=self.feedback_callback)

robot_name= None

def movebase_client(factory_task_msg):
    global robot_name
    #MOdify this to not be hardcoded
    '''
    IDEAS:
        TODO: Wrapper around each robot_n/move_base/ to calculate distance to point and determine cost
        - In multirobotlaunch lauch a node for each robot that simulates this behaviour and serves as an interface between the action client and 
        the central production planner. DONE
        TODO: Modify this script to listen to TaskAuction, contact the cost calculation service and publish to TaskBid
    '''
    # Calculate cost
    cost = random.randint(1,100)
    # Place bid
    pub = rospy.Publisher('TaskBids', TaskBid, queue_size=10, latch=True)
    task_bid = TaskBid()
    task_bid.robot_name = robot_name
    task_bid.bid = cost
    pub.publish(task_bid)
    print("Published bid: ", str(task_bid.bid))
    # If we won the bid then generate the goal for move_base 
    wonAuction = False              
    if(wonAuction):
        client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "/map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(3.35762906956, -0.224057200965, 0), Quaternion(0.0, 0.0, -0.698491025714, 0.715618814032))

        client.send_goal(goal)
        wait = client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return client.get_result()

if __name__ == '__main__':
    try:
        robot_name="default"
        if len(sys.argv)>= 2:
            robot_name = sys.argv[1]
        rospy.init_node('robot_goal_provider')
        print ('Number of arguments:', len(sys.argv), 'arguments.')
        print ('Argument List:', str(sys.argv))
        rospy.Subscriber("TaskAuction", FactoryTask, movebase_client)
        # Keep up until node is finished
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")