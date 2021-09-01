#!/usr/bin/env python
import rospy
import actionlib
from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
class StateMachine:
    def __init__(self):
        self.client = actionlib.SimpleActionClient('/dashgo_0/move_base', MoveBaseAction)
        #ROS Subscribers
        
        pass
    def do_mission(self):
        self.client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "/map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(goal_path[index][0], goal_path[index][1], 0), Quaternion(goal_path[index][2],goal_path[index][3],goal_path[index][4],goal_path[index][5]))
        self.client.send_goal(goal)
        print("Goal to dashgo 0 sent")
        wait = self.client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
            return None
        else:
            return self.client.get_result()
# goal_path = [
#     [1.832814,1.753299,0.000000,0.000000,-0.710403,0.703795],
#     [5.425715,4.625706,0.000000,0.000000,-0.000100,1.000000]
# ]


if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        while not rospy.is_shutdown():
            robot.do_mission()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")