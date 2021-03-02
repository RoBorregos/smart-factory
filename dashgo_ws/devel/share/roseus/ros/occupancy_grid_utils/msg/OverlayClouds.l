;; Auto-generated. Do not edit!


(when (boundp 'occupancy_grid_utils::OverlayClouds)
  (if (not (find-package "OCCUPANCY_GRID_UTILS"))
    (make-package "OCCUPANCY_GRID_UTILS"))
  (shadow 'OverlayClouds (find-package "OCCUPANCY_GRID_UTILS")))
(unless (find-package "OCCUPANCY_GRID_UTILS::OVERLAYCLOUDS")
  (make-package "OCCUPANCY_GRID_UTILS::OVERLAYCLOUDS"))

(in-package "ROS")
;;//! \htmlinclude OverlayClouds.msg.html
(if (not (find-package "NAV_MSGS"))
  (ros::roseus-add-msgs "nav_msgs"))


(defclass occupancy_grid_utils::OverlayClouds
  :super ros::object
  :slots (_grid _frame_id _occupancy_threshold _max_distance _min_pass_through _hit_counts _pass_through_counts ))

(defmethod occupancy_grid_utils::OverlayClouds
  (:init
   (&key
    ((:grid __grid) (instance nav_msgs::OccupancyGrid :init))
    ((:frame_id __frame_id) "")
    ((:occupancy_threshold __occupancy_threshold) 0.0)
    ((:max_distance __max_distance) 0.0)
    ((:min_pass_through __min_pass_through) 0.0)
    ((:hit_counts __hit_counts) (make-array 0 :initial-element 0 :element-type :integer))
    ((:pass_through_counts __pass_through_counts) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _grid __grid)
   (setq _frame_id (string __frame_id))
   (setq _occupancy_threshold (float __occupancy_threshold))
   (setq _max_distance (float __max_distance))
   (setq _min_pass_through (float __min_pass_through))
   (setq _hit_counts __hit_counts)
   (setq _pass_through_counts __pass_through_counts)
   self)
  (:grid
   (&rest __grid)
   (if (keywordp (car __grid))
       (send* _grid __grid)
     (progn
       (if __grid (setq _grid (car __grid)))
       _grid)))
  (:frame_id
   (&optional __frame_id)
   (if __frame_id (setq _frame_id __frame_id)) _frame_id)
  (:occupancy_threshold
   (&optional __occupancy_threshold)
   (if __occupancy_threshold (setq _occupancy_threshold __occupancy_threshold)) _occupancy_threshold)
  (:max_distance
   (&optional __max_distance)
   (if __max_distance (setq _max_distance __max_distance)) _max_distance)
  (:min_pass_through
   (&optional __min_pass_through)
   (if __min_pass_through (setq _min_pass_through __min_pass_through)) _min_pass_through)
  (:hit_counts
   (&optional __hit_counts)
   (if __hit_counts (setq _hit_counts __hit_counts)) _hit_counts)
  (:pass_through_counts
   (&optional __pass_through_counts)
   (if __pass_through_counts (setq _pass_through_counts __pass_through_counts)) _pass_through_counts)
  (:serialization-length
   ()
   (+
    ;; nav_msgs/OccupancyGrid _grid
    (send _grid :serialization-length)
    ;; string _frame_id
    4 (length _frame_id)
    ;; float32 _occupancy_threshold
    4
    ;; float32 _max_distance
    4
    ;; float32 _min_pass_through
    4
    ;; int32[] _hit_counts
    (* 4    (length _hit_counts)) 4
    ;; int32[] _pass_through_counts
    (* 4    (length _pass_through_counts)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; nav_msgs/OccupancyGrid _grid
       (send _grid :serialize s)
     ;; string _frame_id
       (write-long (length _frame_id) s) (princ _frame_id s)
     ;; float32 _occupancy_threshold
       (sys::poke _occupancy_threshold (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _max_distance
       (sys::poke _max_distance (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _min_pass_through
       (sys::poke _min_pass_through (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32[] _hit_counts
     (write-long (length _hit_counts) s)
     (dotimes (i (length _hit_counts))
       (write-long (elt _hit_counts i) s)
       )
     ;; int32[] _pass_through_counts
     (write-long (length _pass_through_counts) s)
     (dotimes (i (length _pass_through_counts))
       (write-long (elt _pass_through_counts i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; nav_msgs/OccupancyGrid _grid
     (send _grid :deserialize buf ptr-) (incf ptr- (send _grid :serialization-length))
   ;; string _frame_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _frame_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _occupancy_threshold
     (setq _occupancy_threshold (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _max_distance
     (setq _max_distance (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _min_pass_through
     (setq _min_pass_through (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32[] _hit_counts
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _hit_counts (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _hit_counts i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _pass_through_counts
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pass_through_counts (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _pass_through_counts i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get occupancy_grid_utils::OverlayClouds :md5sum-) "a1dfac662600ca9b91b434a76485a5d9")
(setf (get occupancy_grid_utils::OverlayClouds :datatype-) "occupancy_grid_utils/OverlayClouds")
(setf (get occupancy_grid_utils::OverlayClouds :definition-)
      "nav_msgs/OccupancyGrid grid
string frame_id
float32 occupancy_threshold
float32 max_distance
float32 min_pass_through
int32[] hit_counts
int32[] pass_through_counts
================================================================================
MSG: nav_msgs/OccupancyGrid
# This represents a 2-D grid map, in which each cell represents the probability of
# occupancy.

Header header 

#MetaData for the map
MapMetaData info

# The map data, in row-major order, starting with (0,0).  Occupancy
# probabilities are in the range [0,100].  Unknown is -1.
int8[] data

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
MSG: nav_msgs/MapMetaData
# This hold basic information about the characterists of the OccupancyGrid

# The time at which the map was loaded
time map_load_time
# The map resolution [m/cell]
float32 resolution
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin
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

")



(provide :occupancy_grid_utils/OverlayClouds "a1dfac662600ca9b91b434a76485a5d9")


