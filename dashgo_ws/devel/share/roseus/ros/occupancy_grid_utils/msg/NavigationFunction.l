;; Auto-generated. Do not edit!


(when (boundp 'occupancy_grid_utils::NavigationFunction)
  (if (not (find-package "OCCUPANCY_GRID_UTILS"))
    (make-package "OCCUPANCY_GRID_UTILS"))
  (shadow 'NavigationFunction (find-package "OCCUPANCY_GRID_UTILS")))
(unless (find-package "OCCUPANCY_GRID_UTILS::NAVIGATIONFUNCTION")
  (make-package "OCCUPANCY_GRID_UTILS::NAVIGATIONFUNCTION"))

(in-package "ROS")
;;//! \htmlinclude NavigationFunction.msg.html
(if (not (find-package "NAV_MSGS"))
  (ros::roseus-add-msgs "nav_msgs"))


(defclass occupancy_grid_utils::NavigationFunction
  :super ros::object
  :slots (_info _source _valid _back_pointers _potential ))

(defmethod occupancy_grid_utils::NavigationFunction
  (:init
   (&key
    ((:info __info) (instance nav_msgs::MapMetaData :init))
    ((:source __source) 0)
    ((:valid __valid) (let (r) (dotimes (i 0) (push nil r)) r))
    ((:back_pointers __back_pointers) (make-array 0 :initial-element 0 :element-type :integer))
    ((:potential __potential) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _info __info)
   (setq _source (round __source))
   (setq _valid __valid)
   (setq _back_pointers __back_pointers)
   (setq _potential __potential)
   self)
  (:info
   (&rest __info)
   (if (keywordp (car __info))
       (send* _info __info)
     (progn
       (if __info (setq _info (car __info)))
       _info)))
  (:source
   (&optional __source)
   (if __source (setq _source __source)) _source)
  (:valid
   (&optional __valid)
   (if __valid (setq _valid __valid)) _valid)
  (:back_pointers
   (&optional __back_pointers)
   (if __back_pointers (setq _back_pointers __back_pointers)) _back_pointers)
  (:potential
   (&optional __potential)
   (if __potential (setq _potential __potential)) _potential)
  (:serialization-length
   ()
   (+
    ;; nav_msgs/MapMetaData _info
    (send _info :serialization-length)
    ;; uint32 _source
    4
    ;; bool[] _valid
    (* 1    (length _valid)) 4
    ;; uint32[] _back_pointers
    (* 4    (length _back_pointers)) 4
    ;; float32[] _potential
    (* 4    (length _potential)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; nav_msgs/MapMetaData _info
       (send _info :serialize s)
     ;; uint32 _source
       (write-long _source s)
     ;; bool[] _valid
     (write-long (length _valid) s)
     (dotimes (i (length _valid))
       (if (elt _valid i) (write-byte -1 s) (write-byte 0 s))
       )
     ;; uint32[] _back_pointers
     (write-long (length _back_pointers) s)
     (dotimes (i (length _back_pointers))
       (write-long (elt _back_pointers i) s)
       )
     ;; float32[] _potential
     (write-long (length _potential) s)
     (dotimes (i (length _potential))
       (sys::poke (elt _potential i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; nav_msgs/MapMetaData _info
     (send _info :deserialize buf ptr-) (incf ptr- (send _info :serialization-length))
   ;; uint32 _source
     (setq _source (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool[] _valid
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _valid (make-list n))
     (dotimes (i n)
     (setf (elt _valid i) (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
     ))
   ;; uint32[] _back_pointers
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _back_pointers (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _back_pointers i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; float32[] _potential
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _potential (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _potential i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get occupancy_grid_utils::NavigationFunction :md5sum-) "c75461ff4f50ec30d6191b0a4430e7ee")
(setf (get occupancy_grid_utils::NavigationFunction :datatype-) "occupancy_grid_utils/NavigationFunction")
(setf (get occupancy_grid_utils::NavigationFunction :definition-)
      "nav_msgs/MapMetaData info
uint32 source
bool[] valid
uint32[] back_pointers
float32[] potential
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



(provide :occupancy_grid_utils/NavigationFunction "c75461ff4f50ec30d6191b0a4430e7ee")


