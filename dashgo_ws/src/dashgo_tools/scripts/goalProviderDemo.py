#!/usr/bin/env python
import rospy
import actionlib
from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

goal_path = [
    [0.115000,-0.000000,0.000000,0.000000,-0.000000,1.000000],
    [6.028582,-0.655752,0.000000,0.000000,0.714575,0.699559],
    [6.717341,-3.081526,0.000000,0.000000,-0.718903,0.695111],
    [9.028191,-7.060456,0.000000,0.000000,0.001121,0.999999],
    [7.403815,4.477918,0.000000,0.000000,0.999805,0.019732],
    [5.677878,7.266975,0.000000,0.000000,0.707953,0.706260],
    [0.207015,-0.054385,0.000000,0.000000,0.008553,0.999963]
]

process_list = [
    [3,1],
    [2,3],
    [4,5]
]

def movebase_client(index):
    client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "/map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose = Pose(Point(goal_path[index][0], goal_path[index][1], 0), Quaternion(goal_path[index][2],goal_path[index][3],goal_path[index][4],goal_path[index][5]))
    client.send_goal(goal)
    print("Goal to dashgo sent")

    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
        return None
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('goal_provider_1')
        for process in process_list:
            for process_step in process:
                result = movebase_client(process_step)
                if result:
                    rospy.loginfo("Goal execution done!")
                else:
                    rospy.loginfo("Goal failed!")
                    exit(0)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
