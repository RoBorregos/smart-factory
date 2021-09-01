#!/usr/bin/env python
import rospy
import actionlib
from geometry_msgs.msg import Pose, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
# goal_path = [
#     [1.832814,1.753299,0.000000,0.000000,-0.710403,0.703795],
#     [5.425715,4.625706,0.000000,0.000000,-0.000100,1.000000]
# ]
class StateMachine:
    def __init__(self):
        self.client = actionlib.SimpleActionClient('/dashgo_0/move_base', MoveBaseAction)
    def do_mission(self, plcregisters):
        self.client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "/map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(goal_path[plcregisters[0]][0], goal_path[plcregisters[1]][1], 0), Quaternion(goal_path[plcregisters[2]][2],goal_path[plcregisters[3]][3],goal_path[plcregisters[4]][4],goal_path[plcregisters[5]][5]))
        self.client.send_goal(goal)
        print("Goal to dashgo 0 sent")
        wait = self.client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
            return None
        else:
            return self.client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('statemachine')
        robot = StateMachine()
        while not rospy.is_shutdown():
            try:
                client =  ModbusClient("192.168.100.23",port=502)
                UNIT = 0x1
                conexion = client.connect()
                rospy.logwarn("Modbus connection ready")
            except Exception as error:
                rospy.logwarn("Modbus connection error")
                rospy.logwarn(error)
            try:
                rr = self.client.read_holding_registers(0,26,unit=self.UNIT)
                self.client.close()
                rospy.logwarn(rr.registers)
                rospy.logwarn("PLC-DASHGO working")
                robot.do_mission(rr.registers)
                rospy.sleep(1)
            except Exception as error:
                rospy.logwarn("Reading registers not ready")
                rospy.logwarn(error)   
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")