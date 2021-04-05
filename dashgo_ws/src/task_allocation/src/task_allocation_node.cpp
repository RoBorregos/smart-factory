#include "ros/ros.h"
#include "task_allocation/FactoryTask.h"
#include <string>

class TaskAllocator
{

private:
    // ROS
    ros::NodeHandle* node_handle;
    ros::Publisher* task_auction_pub;
    ros::Suscriber* task_bids_sus;

    // Bidder information
    int top_bidder;
    int top_bidder_cost;

    // Constants
    const static string NODE_NAME = "TaskAllocator";
    const static string PUBLISHER_TOPIC_NAME = "TaskAuction";
};

TaskAllocator::TaskAllocator()
{
    ros::init(argc, argv, NODE_NAME);
    node_handle = new ros::NodeHandle;
    task_auction_pub = new node_handle.advertise<central::FactoryTask>(PUBLISHER_TOPIC_NAME, 1000);
}

TaskAllocator::publish_new_task(central::FactoryTask new_task){

}



int main(int argc, char **argv)
{
    TaskAllocator TaskAllocator();
    return 0;
}