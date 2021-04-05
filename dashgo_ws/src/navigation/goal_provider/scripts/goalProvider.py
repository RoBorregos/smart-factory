#!/usr/bin/env python
import rospy
import actionlib
from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# goal = MoveBaseGoal()
# goal.target_pose.pose = Pose(Point(1.5, -4.85, 0), Quaternion(0.0, 0.0, 0.6, 0.77))
# goal.target_pose.header.frame_id = "map" 
# goal.target_pose.header.stamp = rospy.Time() 
# self.sac.send_goal(goal, active_cb=self.active_callback, done_cb=self.done_callback, feedback_cb=self.feedback_callback)



def movebase_client():
    client = actionlib.SimpleActionClient('/robot_0/move_base', MoveBaseAction)
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
        rospy.init_node('goal_provider')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")