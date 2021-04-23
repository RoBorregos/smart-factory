#include "ros/ros.h"
#include <ros/console.h>
#include "std_msgs/Float32.h"

#include <string>
#include <iostream>
#include <memory>
#include <vector>

#include "task_allocation/FactoryTask.h"
#include "task_allocation/TaskBid.h"

enum ActionTypes : short
{
    GO_TO_ACTION,
    DUMMY
};

struct Bid
{
    float robot_name;
    float cost;
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
    static void received_bid(const std_msgs::Float32::ConstPtr &msg);

private:
    // ROS
    std::unique_ptr<ros::NodeHandle> node_handle;
    ros::Publisher task_auction_pub;
    ros::Subscriber task_bids_subs;

    // Bidder information
    int top_bidder;
    int top_bidder_cost;
    static std::vector<Bid> bids_queue;
    bool ASK_CONSOLE_INPUT;

    // Constants
    static std::string NODE_NAME;
    static std::string PUBLISHER_TOPIC_NAME;
    static std::string SUBSCRIBER_TOPIC_NAME;

    // Methods
    void wait_for_bids(int time_out);
};

TaskAllocator::TaskAllocator(int argc, char **argv)
{

    ros::init(argc, argv, NODE_NAME);
    node_handle = make_unique<ros::NodeHandle>();
    task_auction_pub = node_handle->advertise<task_allocation::FactoryTask>(PUBLISHER_TOPIC_NAME, 1000);
    task_bids_subs = node_handle->subscribe(SUBSCRIBER_TOPIC_NAME, 1000, this->received_bid);
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
    // TODO: DEBUG THIS
    if (ros::ok())
    {
        ROS_DEBUG("Publishing new task...");
        ROS_DEBUG(task_auction_pub.getTopic());
        task_auction_pub.publish(new_task);
        ros::spinOnce();
    }
}

void TaskAllocator::received_bid(const std_msgs::Float32::ConstPtr &msg)
{
    Bid new_bid;
    new_bid.robot_name = 0;
    new_bid.cost = msg->data;
    bids_queue.push_back(new_bid);
}

void TaskAllocator::wait_for_bids(int timeout)
{
    ros::Time begin = ros::Time::now();
    ros::Time wait_time(timeout);
    while (ros::ok() && begin < wait_time)
    {
        ros::spinOnce();
    }
    // Process bids
}

std::string TaskAllocator::PUBLISHER_TOPIC_NAME = "TaskAuction";
std::string TaskAllocator::SUBSCRIBER_TOPIC_NAME = "TaskBids";
std::string TaskAllocator::NODE_NAME = "TaskAllocatorNode";
std::vector<Bid> TaskAllocator::bids_queue = std::vector<Bid>();

int main(int argc, char **argv)
{
    if (ros::console::set_logger_level(ROSCONSOLE_DEFAULT_NAME, ros::console::levels::Debug))
    {
        ros::console::notifyLoggerLevelsChanged();
    }

    TaskAllocator taskAllocator(argc, argv);
    if (argc == 2)
    {
        std::cout << argc << " " << argv[1] << std::endl;
        // Check if flag equals user input
        if ((std::string)argv[1] == "y")
        {
            std::cout << "yes receive user input" << std::endl;
            taskAllocator.console_input_tasks();
        }
    }
    else
    {
        taskAllocator.demo_task();
    }

    return 0;
}