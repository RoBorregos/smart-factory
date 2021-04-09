#include "ros/ros.h"
#include <ros/console.h>

#include <string>
#include <iostream>
#include <memory>
#include <vector>

#include "task_allocation/FactoryTask.h"

enum ActionTypes : short
{
    GO_TO_ACTION,
    DUMMY
};

// make_unique not available in C++11
template <typename T, typename... Args>
std::unique_ptr<T> make_unique(Args &&...args)
{
    return std::unique_ptr<T>(new T(std::forward<Args>(args)...));
}

class TaskAllocator
{

public:
    TaskAllocator(int argc, char **argv);
    void publish_new_task(task_allocation::FactoryTask new_task);
    void console_input_tasks();
    void demo_task();

private:
    // ROS
    std::unique_ptr<ros::NodeHandle> node_handle;
    ros::Publisher task_auction_pub;
    ros::Subscriber task_bids_sus;

    // Bidder information
    int top_bidder;
    int top_bidder_cost;
    bool ASK_CONSOLE_INPUT;

    // Constants
    static std::string NODE_NAME;
    static std::string PUBLISHER_TOPIC_NAME;
};

TaskAllocator::TaskAllocator(int argc, char **argv)
{

    ros::init(argc, argv, NODE_NAME);
    node_handle = make_unique<ros::NodeHandle>();
    task_auction_pub = node_handle->advertise<task_allocation::FactoryTask>(PUBLISHER_TOPIC_NAME, 1000);
    ROS_DEBUG("Initialized TaskAllocator");
    ASK_CONSOLE_INPUT = true;
}

void ::TaskAllocator::demo_task()
{
    short userInputActionType = 0;
    std::string target_position = "3.357629,-0.224057,0.000000,0.000000,-0.698491,0.715619";

    // Ask for user input of new task and pusblish it
    task_allocation::FactoryTask new_factory_task;
    ROS_DEBUG("Total number of actions registered in system %lu", sizeof(ActionTypes) / sizeof(GO_TO_ACTION));
    new_factory_task.actionType = userInputActionType;

    // Generate target locating in string format
    // "3.357629,-0.224057,0.000000,0.000000,-0.698491,0.715619"
    // PointX,PointY,PointZ, QuaternionX, QuaternionY, QuaternionZ, QuaternionW
    new_factory_task.params.push_back(target_position);
    publish_new_task(new_factory_task);
}

void TaskAllocator::console_input_tasks()
{
    short userInputActionType = 0;
    std::string target_position = "3.357629,-0.224057,0.000000,0.000000,-0.698491,0.715619";

    while (ros::ok)
    {
        // Ask for user input of new task and pusblish it
        task_allocation::FactoryTask new_factory_task;
        ROS_DEBUG("Total number of actions registered in system %lu", sizeof(ActionTypes) / sizeof(GO_TO_ACTION));
        if (ASK_CONSOLE_INPUT)
        {
            std::cout << "Please input the actionType of the task (number): ";
            std::cin >> userInputActionType;
        }

        // Verify input
        if (userInputActionType < static_cast<short>(GO_TO_ACTION) || userInputActionType >= sizeof(ActionTypes) / sizeof(GO_TO_ACTION))
            continue;
        new_factory_task.actionType = userInputActionType;

        // Generate target locating in string format
        // "3.357629,-0.224057,0.000000,0.000000,-0.698491,0.715619"
        // PointX,PointY,PointZ, QuaternionX, QuaternionY, QuaternionZ, QuaternionW
        if (ASK_CONSOLE_INPUT)
        {
            std::cout << "Please input the target position in the format"
                      << "PointX,PointY,PointZ, QuaternionX, QuaternionY, QuaternionZ, QuaternionW :" << std::endl;

            std::cin >> target_position;
        }

        new_factory_task.params.push_back(target_position);
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
    if (argc == 2)
    {
        std::cout << argc << " " << argv[1]<< std::endl;
        // Check if flag equals user input
        if ((std::string)argv[1] == "y")
        {
            std::cout <<"yes receive user input"<< std::endl;
            taskAllocator.console_input_tasks();
        }
    }
    else
    {
        taskAllocator.demo_task();
    }

    return 0;
}