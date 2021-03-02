;; Auto-generated. Do not edit!


(when (boundp 'occupancy_grid_utils::LocalizedCloud)
  (if (not (find-package "OCCUPANCY_GRID_UTILS"))
    (make-package "OCCUPANCY_GRID_UTILS"))
  (shadow 'LocalizedCloud (find-package "OCCUPANCY_GRID_UTILS")))
(unless (find-package "OCCUPANCY_GRID_UTILS::LOCALIZEDCLOUD")
  (make-package "OCCUPANCY_GRID_UTILS::LOCALIZEDCLOUD"))

(in-package "ROS")
;;//! \htmlinclude LocalizedCloud.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass occupancy_grid_utils::LocalizedCloud
  :super ros::object
  :slots (_header _sensor_pose _cloud ))

(defmethod occupancy_grid_utils::LocalizedCloud
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:sensor_pose __sensor_pose) (instance geometry_msgs::Pose :init))
    ((:cloud __cloud) (instance sensor_msgs::PointCloud :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _sensor_pose __sensor_pose)
   (setq _cloud __cloud)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:sensor_pose
   (&rest __sensor_pose)
   (if (keywordp (car __sensor_pose))
       (send* _sensor_pose __sensor_pose)
     (progn
       (if __sensor_pose (setq _sensor_pose (car __sensor_pose)))
       _sensor_pose)))
  (:cloud
   (&rest __cloud)
   (if (keywordp (car __cloud))
       (send* _cloud __cloud)
     (progn
       (if __cloud (setq _cloud (car __cloud)))
       _cloud)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; geometry_msgs/Pose _sensor_pose
    (send _sensor_pose :serialization-length)
    ;; sensor_msgs/PointCloud _cloud
    (send _cloud :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; geometry_msgs/Pose _sensor_pose
       (send _sensor_pose :serialize s)
     ;; sensor_msgs/PointCloud _cloud
       (send _cloud :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; geometry_msgs/Pose _sensor_pose
     (send _sensor_pose :deserialize buf ptr-) (incf ptr- (send _sensor_pose :serialization-length))
   ;; sensor_msgs/PointCloud _cloud
     (send _cloud :deserialize buf ptr-) (incf ptr- (send _cloud :serialization-length))
   ;;
   self)
  )

(setf (get occupancy_grid_utils::LocalizedCloud :md5sum-) "e868d77f7e7116b7eb215e43caa0ea5d")
(setf (get occupancy_grid_utils::LocalizedCloud :datatype-) "occupancy_grid_utils/LocalizedCloud")
(setf (get occupancy_grid_utils::LocalizedCloud :definition-)
      "# Represents a point cloud (in a sensor frame) together with the pose of the sensor in
# reference frame header.frame_id
# The header of the cloud is ignored
Header header
geometry_msgs/Pose sensor_pose
sensor_msgs/PointCloud cloud
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: sensor_msgs/PointCloud
# This message holds a collection of 3d points, plus optional additional
# information about each point.

# Time of sensor data acquisition, coordinate frame ID.
Header header

# Array of 3d points. Each Point32 should be interpreted as a 3d point
# in the frame given in the header.
geometry_msgs/Point32[] points

# Each channel should have the same number of elements as points array,
# and the data in each channel should correspond 1:1 with each point.
# Channel names in common practice are listed in ChannelFloat32.msg.
ChannelFloat32[] channels

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
================================================================================
MSG: sensor_msgs/ChannelFloat32
# This message is used by the PointCloud message to hold optional data
# associated with each point in the cloud. The length of the values
# array should be the same as the length of the points array in the
# PointCloud, and each value should be associated with the corresponding
# point.

# Channel names in existing practice include:
#   \"u\", \"v\" - row and column (respectively) in the left stereo image.
#              This is opposite to usual conventions but remains for
#              historical reasons. The newer PointCloud2 message has no
#              such problem.
#   \"rgb\" - For point clouds produced by color stereo cameras. uint8
#           (R,G,B) values packed into the least significant 24 bits,
#           in order.
#   \"intensity\" - laser or pixel intensity.
#   \"distance\"

# The channel name should give semantics of the channel (e.g.
# \"intensity\" instead of \"value\").
string name

# The values array should be 1-1 with the elements of the associated
# PointCloud.
float32[] values

")



(provide :occupancy_grid_utils/LocalizedCloud "e868d77f7e7116b7eb215e43caa0ea5d")


