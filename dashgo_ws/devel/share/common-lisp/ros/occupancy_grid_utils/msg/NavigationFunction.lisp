; Auto-generated. Do not edit!


(cl:in-package occupancy_grid_utils-msg)


;//! \htmlinclude NavigationFunction.msg.html

(cl:defclass <NavigationFunction> (roslisp-msg-protocol:ros-message)
  ((info
    :reader info
    :initarg :info
    :type nav_msgs-msg:MapMetaData
    :initform (cl:make-instance 'nav_msgs-msg:MapMetaData))
   (source
    :reader source
    :initarg :source
    :type cl:integer
    :initform 0)
   (valid
    :reader valid
    :initarg :valid
    :type (cl:vector cl:boolean)
   :initform (cl:make-array 0 :element-type 'cl:boolean :initial-element cl:nil))
   (back_pointers
    :reader back_pointers
    :initarg :back_pointers
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (potential
    :reader potential
    :initarg :potential
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass NavigationFunction (<NavigationFunction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NavigationFunction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NavigationFunction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name occupancy_grid_utils-msg:<NavigationFunction> is deprecated: use occupancy_grid_utils-msg:NavigationFunction instead.")))

(cl:ensure-generic-function 'info-val :lambda-list '(m))
(cl:defmethod info-val ((m <NavigationFunction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:info-val is deprecated.  Use occupancy_grid_utils-msg:info instead.")
  (info m))

(cl:ensure-generic-function 'source-val :lambda-list '(m))
(cl:defmethod source-val ((m <NavigationFunction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:source-val is deprecated.  Use occupancy_grid_utils-msg:source instead.")
  (source m))

(cl:ensure-generic-function 'valid-val :lambda-list '(m))
(cl:defmethod valid-val ((m <NavigationFunction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:valid-val is deprecated.  Use occupancy_grid_utils-msg:valid instead.")
  (valid m))

(cl:ensure-generic-function 'back_pointers-val :lambda-list '(m))
(cl:defmethod back_pointers-val ((m <NavigationFunction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:back_pointers-val is deprecated.  Use occupancy_grid_utils-msg:back_pointers instead.")
  (back_pointers m))

(cl:ensure-generic-function 'potential-val :lambda-list '(m))
(cl:defmethod potential-val ((m <NavigationFunction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader occupancy_grid_utils-msg:potential-val is deprecated.  Use occupancy_grid_utils-msg:potential instead.")
  (potential m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NavigationFunction>) ostream)
  "Serializes a message object of type '<NavigationFunction>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'info) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'source)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'source)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'source)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'source)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'valid))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if ele 1 0)) ostream))
   (cl:slot-value msg 'valid))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'back_pointers))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'back_pointers))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'potential))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'potential))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NavigationFunction>) istream)
  "Deserializes a message object of type '<NavigationFunction>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'info) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'source)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'source)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'source)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'source)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'valid) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'valid)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:not (cl:zerop (cl:read-byte istream)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'back_pointers) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'back_pointers)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'potential) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'potential)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NavigationFunction>)))
  "Returns string type for a message object of type '<NavigationFunction>"
  "occupancy_grid_utils/NavigationFunction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NavigationFunction)))
  "Returns string type for a message object of type 'NavigationFunction"
  "occupancy_grid_utils/NavigationFunction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NavigationFunction>)))
  "Returns md5sum for a message object of type '<NavigationFunction>"
  "c75461ff4f50ec30d6191b0a4430e7ee")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NavigationFunction)))
  "Returns md5sum for a message object of type 'NavigationFunction"
  "c75461ff4f50ec30d6191b0a4430e7ee")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NavigationFunction>)))
  "Returns full string definition for message of type '<NavigationFunction>"
  (cl:format cl:nil "nav_msgs/MapMetaData info~%uint32 source~%bool[] valid~%uint32[] back_pointers~%float32[] potential~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NavigationFunction)))
  "Returns full string definition for message of type 'NavigationFunction"
  (cl:format cl:nil "nav_msgs/MapMetaData info~%uint32 source~%bool[] valid~%uint32[] back_pointers~%float32[] potential~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NavigationFunction>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'info))
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'valid) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'back_pointers) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'potential) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NavigationFunction>))
  "Converts a ROS message object to a list"
  (cl:list 'NavigationFunction
    (cl:cons ':info (info msg))
    (cl:cons ':source (source msg))
    (cl:cons ':valid (valid msg))
    (cl:cons ':back_pointers (back_pointers msg))
    (cl:cons ':potential (potential msg))
))
