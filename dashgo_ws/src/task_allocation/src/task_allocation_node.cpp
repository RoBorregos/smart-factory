#include "ros/ros.h"
#include <ros/console.h>
#include "task_allocation/FactoryTask.h"
#include <string>
#include <iostream>

enum ActionTypes : short{
    GO_TO_ACTION,
    DUMMY
};


class TaskAllocator
{

public:
    TaskAllocator(int argc, char **argv);
    ~TaskAllocator();
    void publish_new_task(task_allocation::FactoryTask new_task);
    void console_input_tasks();

private:

    // ROS
    ros::NodeHandle *node_handle;
    ros::Publisher task_auction_pub;
    ros::Subscriber task_bids_sus;

    // Bidder information
    int top_bidder;
    int top_bidder_cost;

    // Constants
    static std::string NODE_NAME;
    static std::string PUBLISHER_TOPIC_NAME;
};

TaskAllocator::TaskAllocator(int argc, char **argv)
{

    ros::init(argc, argv, NODE_NAME);
    node_handle = new ros::NodeHandle();
    task_auction_pub = node_handle->advertise<task_allocation::FactoryTask>(PUBLISHER_TOPIC_NAME, 1000);
    ROS_DEBUG("Initialized TaskAllocator");
}

TaskAllocator::~TaskAllocator()
{
    delete node_handle;
}

void TaskAllocator::console_input_tasks()
{
    short userInputActionType;

    while (ros::ok)
    {
        // Ask for user input of new task and pusblish it
        task_allocation::FactoryTask new_factory_task;
        std::cout << "Please input the actionType of the task (number): ";
        std::cin >> userInputActionType;
        ROS_DEBUG("Number of actions registered %lu",sizeof(ActionTypes)/sizeof(GO_TO_ACTION));
        if(userInputActionType<static_cast<short>(GO_TO_ACTION) || userInputActionType>=sizeof(ActionTypes)/sizeof(GO_TO_ACTION))
            continue;
        new_factory_task.actionType = userInputActionType;        
        publish_new_task(new_factory_task);
    }
}

void TaskAllocator::publish_new_task(task_allocation::FactoryTask new_task)
{
    ROS_DEBUG("Publishing new task...");
    task_auction_pub.publish(new_task);
}

std::string TaskAllocator::PUBLISHER_TOPIC_NAME = "TaskAuction";
std::string TaskAllocator::NODE_NAME = "TaskAllocatorNode";

int main(int argc, char **argv)
{
    if (ros::console::set_logger_level(ROSCONSOLE_DEFAULT_NAME, ros::console::levels::Debug))
    {
        ros::console::notifyLoggerLevelsChanged();
    }

    TaskAllocator taskAllocator(argc, argv);
    taskAllocator.console_input_tasks();
    return 0;
}