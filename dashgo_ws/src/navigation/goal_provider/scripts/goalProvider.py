#!/usr/bin/env python
import rospy
import actionlib
from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

goal_path = [
    [2.047112,5.325517,0.000000,0.000000,0.706755,0.707459],
    [1.832814,1.753299,0.000000,0.000000,-0.710403,0.703795],
    [5.425715,4.625706,0.000000,0.000000,-0.000100,1.000000]
]


def movebase_client(index):
    #Modify this to not be hardcoded
    '''
    IDEAS:
        - Wrapper around each robot_n/move_base/ to calculate distance to point and determine cost
        - In multirobotlaunch lauch a node for each robot that simulates this behaviour and serves as an interface between the action client0 and 
        the central production planner.
    '''
    client = actionlib.SimpleActionClient('/dashgo_0/move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "/map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose = Pose(Point(goal_path[index][0], goal_path[index][1], 0), Quaternion(goal_path[index][2],goal_path[index][3],goal_path[index][4],goal_path[index][5]))
    client.send_goal(goal)
    print("Goal to dashgo 0 sent")

    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
        return None
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('goal_provider_0')
        for i in range(3):
            result = movebase_client(i)
            if result:
                rospy.loginfo("Goal execution done!")
            else:
                rospy.loginfo("Goal failed!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")