; Auto-generated. Do not edit!


(cl:in-package occupancy_grid_utils-msg)


;//! \htmlinclude OverlayClouds.msg.html

(cl:defclass <OverlayClouds> (roslisp-msg-protocol:ros-message)
  ((grid
    :reader grid
    :initarg :grid
    :type nav_msgs-msg:OccupancyGrid
    :initform (cl:make-instance 'nav_msgs-msg:OccupancyGrid))
   (frame_id
    :reader frame_id
    :initarg :frame_id
    :type cl:string
    :initform "")
   (occupancy_threshold
    :reader occupancy_threshold
    :initarg :occupancy_threshold
    :type cl:float
    :initform 0.0)
   (max_distance
    :reader max_distance
    :initarg :max_distance
    :type cl:float
    :initform 0.0)
   (min_pass_through
    :reader min_pass_through
    :initarg :min_pass_through
    :type cl:float
    :initform 0.0)
   (hit_counts
    :reader hit_counts
    :initarg :hit_counts
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (pass_through_counts
    :reader pass_through_counts
    :initarg :pass_through_counts
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass OverlayClouds (<OverlayClouds>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OverlayClouds>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OverlayClouds)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name occupancy_grid_utils-msg:<OverlayClouds> is deprecated: use occupancy_grid_utils-msg:OverlayClouds instead.")))

(cl:ensure-generic-function 'grid-val :lambda-list '(m))
(cl:defmethod grid-val ((m <OverlayClouds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:grid-val is deprecated.  Use occupancy_grid_utils-msg:grid instead.")
  (grid m))

(cl:ensure-generic-function 'frame_id-val :lambda-list '(m))
(cl:defmethod frame_id-val ((m <OverlayClouds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:frame_id-val is deprecated.  Use occupancy_grid_utils-msg:frame_id instead.")
  (frame_id m))

(cl:ensure-generic-function 'occupancy_threshold-val :lambda-list '(m))
(cl:defmethod occupancy_threshold-val ((m <OverlayClouds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:occupancy_threshold-val is deprecated.  Use occupancy_grid_utils-msg:occupancy_threshold instead.")
  (occupancy_threshold m))

(cl:ensure-generic-function 'max_distance-val :lambda-list '(m))
(cl:defmethod max_distance-val ((m <OverlayClouds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:max_distance-val is deprecated.  Use occupancy_grid_utils-msg:max_distance instead.")
  (max_distance m))

(cl:ensure-generic-function 'min_pass_through-val :lambda-list '(m))
(cl:defmethod min_pass_through-val ((m <OverlayClouds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:min_pass_through-val is deprecated.  Use occupancy_grid_utils-msg:min_pass_through instead.")
  (min_pass_through m))

(cl:ensure-generic-function 'hit_counts-val :lambda-list '(m))
(cl:defmethod hit_counts-val ((m <OverlayClouds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:hit_counts-val is deprecated.  Use occupancy_grid_utils-msg:hit_counts instead.")
  (hit_counts m))

(cl:ensure-generic-function 'pass_through_counts-val :lambda-list '(m))
(cl:defmethod pass_through_counts-val ((m <OverlayClouds>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:pass_through_counts-val is deprecated.  Use occupancy_grid_utils-msg:pass_through_counts instead.")
  (pass_through_counts m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OverlayClouds>) ostream)
  "Serializes a message object of type '<OverlayClouds>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'grid) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'frame_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'frame_id))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'occupancy_threshold))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'max_distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'min_pass_through))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'hit_counts))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'hit_counts))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pass_through_counts))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'pass_through_counts))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OverlayClouds>) istream)
  "Deserializes a message object of type '<OverlayClouds>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'grid) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'frame_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'frame_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'occupancy_threshold) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_distance) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'min_pass_through) (roslisp-utils:decode-single-float-bits bits)))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'hit_counts) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'hit_counts)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pass_through_counts) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pass_through_counts)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OverlayClouds>)))
  "Returns string type for a message object of type '<OverlayClouds>"
  "occupancy_grid_utils/OverlayClouds")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OverlayClouds)))
  "Returns string type for a message object of type 'OverlayClouds"
  "occupancy_grid_utils/OverlayClouds")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OverlayClouds>)))
  "Returns md5sum for a message object of type '<OverlayClouds>"
  "a1dfac662600ca9b91b434a76485a5d9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OverlayClouds)))
  "Returns md5sum for a message object of type 'OverlayClouds"
  "a1dfac662600ca9b91b434a76485a5d9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OverlayClouds>)))
  "Returns full string definition for message of type '<OverlayClouds>"
  (cl:format cl:nil "nav_msgs/OccupancyGrid grid~%string frame_id~%float32 occupancy_threshold~%float32 max_distance~%float32 min_pass_through~%int32[] hit_counts~%int32[] pass_through_counts~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OverlayClouds)))
  "Returns full string definition for message of type 'OverlayClouds"
  (cl:format cl:nil "nav_msgs/OccupancyGrid grid~%string frame_id~%float32 occupancy_threshold~%float32 max_distance~%float32 min_pass_through~%int32[] hit_counts~%int32[] pass_through_counts~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OverlayClouds>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'grid))
     4 (cl:length (cl:slot-value msg 'frame_id))
     4
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'hit_counts) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pass_through_counts) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OverlayClouds>))
  "Converts a ROS message object to a list"
  (cl:list 'OverlayClouds
    (cl:cons ':grid (grid msg))
    (cl:cons ':frame_id (frame_id msg))
    (cl:cons ':occupancy_threshold (occupancy_threshold msg))
    (cl:cons ':max_distance (max_distance msg))
    (cl:cons ':min_pass_through (min_pass_through msg))
    (cl:cons ':hit_counts (hit_counts msg))
    (cl:cons ':pass_through_counts (pass_through_counts msg))
))
