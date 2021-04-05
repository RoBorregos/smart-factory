#include "ros/ros.h"
#include "task_allocation/FactoryTask.h"
#include <string>

class TaskAllocator
{

public:
    TaskAllocator(int argc, char **argv);
    void publish_new_task(task_allocation::FactoryTask new_task);

private:
    // ROS
    ros::NodeHandle* node_handle;
    ros::Publisher* task_auction_pub;
    ros::Subscriber* task_bids_sus;

    // Bidder information
    int top_bidder;
    int top_bidder_cost;

    // Constants
    std::string NODE_NAME;
    const  std::string PUBLISHER_TOPIC_NAME = "TaskAuction";
};

TaskAllocator::TaskAllocator(int argc, char **argv)
{
    
    node_handle = new ros::NodeHandle();
    // *task_auction_pub =  node_handle->advertise<task_allocation::FactoryTask>(PUBLISHER_TOPIC_NAME, 1000);
}

void TaskAllocator::publish_new_task(task_allocation::FactoryTask new_task){

}

int main(int argc, char **argv)
{
    std::string NODE_NAME = "TaskAllocator";
    ros::init(argc, argv, NODE_NAME);
    TaskAllocator TaskAllocator(argc,argv);
    return 0;
}