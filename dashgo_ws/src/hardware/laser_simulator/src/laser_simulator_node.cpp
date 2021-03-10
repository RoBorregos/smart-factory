#include "ros/ros.h"
#include "std_msgs/Bool.h"
#include "nav_msgs/GetMap.h"
#include "geometry_msgs/Pose.h"
#include "geometry_msgs/PoseWithCovarianceStamped.h"
#include "sensor_msgs/LaserScan.h"
#include "tf/transform_listener.h"
#include "occupancy_grid_utils/ray_tracer.h"
#include "random_numbers/random_numbers.h"
#include "ros/ros.h"

int main(int argc, char** argv)
{
    std::cout << "INITIALIZING LASER SIMULATOR..." << std::endl;
    ros::init(argc, argv, "laser_simulator");
    ros::NodeHandle n;
    ros::Rate loop(10);

    float noise = 0;
    if(ros::param::has("~noise"))
        ros::param::get("~noise", noise);

    std::string ns = "";
    if(ros::param::has("~ns"))
        ros::param::get("~ns", ns);
        ns += "/";
    std::cout <<"NS: "<<ns<<std::endl;

    nav_msgs::GetMap srvGetMap;

    std::cout << "Getting static map..." << std::endl;
    ros::service::waitForService("/static_map");
    std::cout << "Static map obtained" << std::endl;
    ros::ServiceClient srvCltGetMap = n.serviceClient<nav_msgs::GetMap>("/static_map");
    srvCltGetMap.call(srvGetMap);
    nav_msgs::OccupancyGrid map = srvGetMap.response.map;

    sensor_msgs::LaserScan scanInfo;
    scanInfo.header.frame_id = ns + "laser_link";
    scanInfo.angle_min = -2;
    scanInfo.angle_max = 2;
    scanInfo.angle_increment = 0.007;
    scanInfo.scan_time = 0.1;
    scanInfo.range_min = 0.01;
    scanInfo.range_max = 4.0;
    sensor_msgs::LaserScan simulatedScan;
    sensor_msgs::LaserScan::Ptr msgFromBag;
    ros::Publisher pubScan = n.advertise<sensor_msgs::LaserScan>("/scan", 1);

    tf::TransformListener listener;
    geometry_msgs::Pose sensorPose;
    sensorPose.position.x = 0;
    sensorPose.position.y = 0;
    sensorPose.position.z = 0;
    sensorPose.orientation.x = 0;
    sensorPose.orientation.y = 0;
    sensorPose.orientation.z = 0;
    sensorPose.orientation.w = 1;

    random_numbers::RandomNumberGenerator rnd;
    while(ros::ok())
    {
        tf::StampedTransform transform;
        tf::Quaternion q;
        try
        {
            listener.lookupTransform("/map", ns + "laser_link", ros::Time(0), transform);
            sensorPose.position.x = transform.getOrigin().x();
            sensorPose.position.y = transform.getOrigin().y();
            q = transform.getRotation();
            sensorPose.orientation.x = q.x();
            sensorPose.orientation.y = q.y();
            sensorPose.orientation.z = q.z();
            sensorPose.orientation.w = q.w();
        }
        catch(...){
            std::cout << "LaserSimulator.-> Cannot get transform from "<<ns<<"laser_link to map" << std::endl;
        }
        
        simulatedScan = *occupancy_grid_utils::simulateRangeScan(map, sensorPose, scanInfo);
        simulatedScan.header.stamp = ros::Time::now();
        if(noise > 0)
            for(int i=0; i<simulatedScan.ranges.size(); i++)
                simulatedScan.ranges[i] += rnd.uniformReal(-noise, noise);
        
        pubScan.publish(simulatedScan);
        ros::spinOnce();
        loop.sleep();
    }
    return 0;
}
