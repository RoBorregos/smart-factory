; Auto-generated. Do not edit!


(cl:in-package occupancy_grid_utils-msg)


;//! \htmlinclude LocalizedCloud.msg.html

(cl:defclass <LocalizedCloud> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (sensor_pose
    :reader sensor_pose
    :initarg :sensor_pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (cloud
    :reader cloud
    :initarg :cloud
    :type sensor_msgs-msg:PointCloud
    :initform (cl:make-instance 'sensor_msgs-msg:PointCloud)))
)

(cl:defclass LocalizedCloud (<LocalizedCloud>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LocalizedCloud>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LocalizedCloud)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name occupancy_grid_utils-msg:<LocalizedCloud> is deprecated: use occupancy_grid_utils-msg:LocalizedCloud instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <LocalizedCloud>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:header-val is deprecated.  Use occupancy_grid_utils-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'sensor_pose-val :lambda-list '(m))
(cl:defmethod sensor_pose-val ((m <LocalizedCloud>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:sensor_pose-val is deprecated.  Use occupancy_grid_utils-msg:sensor_pose instead.")
  (sensor_pose m))

(cl:ensure-generic-function 'cloud-val :lambda-list '(m))
(cl:defmethod cloud-val ((m <LocalizedCloud>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:cloud-val is deprecated.  Use occupancy_grid_utils-msg:cloud instead.")
  (cloud m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LocalizedCloud>) ostream)
  "Serializes a message object of type '<LocalizedCloud>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'sensor_pose) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'cloud) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LocalizedCloud>) istream)
  "Deserializes a message object of type '<LocalizedCloud>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'sensor_pose) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'cloud) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LocalizedCloud>)))
  "Returns string type for a message object of type '<LocalizedCloud>"
  "occupancy_grid_utils/LocalizedCloud")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LocalizedCloud)))
  "Returns string type for a message object of type 'LocalizedCloud"
  "occupancy_grid_utils/LocalizedCloud")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LocalizedCloud>)))
  "Returns md5sum for a message object of type '<LocalizedCloud>"
  "e868d77f7e7116b7eb215e43caa0ea5d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LocalizedCloud)))
  "Returns md5sum for a message object of type 'LocalizedCloud"
  "e868d77f7e7116b7eb215e43caa0ea5d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LocalizedCloud>)))
  "Returns full string definition for message of type '<LocalizedCloud>"
  (cl:format cl:nil "# Represents a point cloud (in a sensor frame) together with the pose of the sensor in~%# reference frame header.frame_id~%# The header of the cloud is ignored~%Header header~%geometry_msgs/Pose sensor_pose~%sensor_msgs/PointCloud cloud~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: sensor_msgs/PointCloud~%# This message holds a collection of 3d points, plus optional additional~%# information about each point.~%~%# Time of sensor data acquisition, coordinate frame ID.~%Header header~%~%# Array of 3d points. Each Point32 should be interpreted as a 3d point~%# in the frame given in the header.~%geometry_msgs/Point32[] points~%~%# Each channel should have the same number of elements as points array,~%# and the data in each channel should correspond 1:1 with each point.~%# Channel names in common practice are listed in ChannelFloat32.msg.~%ChannelFloat32[] channels~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: sensor_msgs/ChannelFloat32~%# This message is used by the PointCloud message to hold optional data~%# associated with each point in the cloud. The length of the values~%# array should be the same as the length of the points array in the~%# PointCloud, and each value should be associated with the corresponding~%# point.~%~%# Channel names in existing practice include:~%#   \"u\", \"v\" - row and column (respectively) in the left stereo image.~%#              This is opposite to usual conventions but remains for~%#              historical reasons. The newer PointCloud2 message has no~%#              such problem.~%#   \"rgb\" - For point clouds produced by color stereo cameras. uint8~%#           (R,G,B) values packed into the least significant 24 bits,~%#           in order.~%#   \"intensity\" - laser or pixel intensity.~%#   \"distance\"~%~%# The channel name should give semantics of the channel (e.g.~%# \"intensity\" instead of \"value\").~%string name~%~%# The values array should be 1-1 with the elements of the associated~%# PointCloud.~%float32[] values~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LocalizedCloud)))
  "Returns full string definition for message of type 'LocalizedCloud"
  (cl:format cl:nil "# Represents a point cloud (in a sensor frame) together with the pose of the sensor in~%# reference frame header.frame_id~%# The header of the cloud is ignored~%Header header~%geometry_msgs/Pose sensor_pose~%sensor_msgs/PointCloud cloud~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: sensor_msgs/PointCloud~%# This message holds a collection of 3d points, plus optional additional~%# information about each point.~%~%# Time of sensor data acquisition, coordinate frame ID.~%Header header~%~%# Array of 3d points. Each Point32 should be interpreted as a 3d point~%# in the frame given in the header.~%geometry_msgs/Point32[] points~%~%# Each channel should have the same number of elements as points array,~%# and the data in each channel should correspond 1:1 with each point.~%# Channel names in common practice are listed in ChannelFloat32.msg.~%ChannelFloat32[] channels~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: sensor_msgs/ChannelFloat32~%# This message is used by the PointCloud message to hold optional data~%# associated with each point in the cloud. The length of the values~%# array should be the same as the length of the points array in the~%# PointCloud, and each value should be associated with the corresponding~%# point.~%~%# Channel names in existing practice include:~%#   \"u\", \"v\" - row and column (respectively) in the left stereo image.~%#              This is opposite to usual conventions but remains for~%#              historical reasons. The newer PointCloud2 message has no~%#              such problem.~%#   \"rgb\" - For point clouds produced by color stereo cameras. uint8~%#           (R,G,B) values packed into the least significant 24 bits,~%#           in order.~%#   \"intensity\" - laser or pixel intensity.~%#   \"distance\"~%~%# The channel name should give semantics of the channel (e.g.~%# \"intensity\" instead of \"value\").~%string name~%~%# The values array should be 1-1 with the elements of the associated~%# PointCloud.~%float32[] values~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LocalizedCloud>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'sensor_pose))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'cloud))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LocalizedCloud>))
  "Converts a ROS message object to a list"
  (cl:list 'LocalizedCloud
    (cl:cons ':header (header msg))
    (cl:cons ':sensor_pose (sensor_pose msg))
    (cl:cons ':cloud (cloud msg))
))
