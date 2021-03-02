# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "occupancy_grid_utils: 3 messages, 0 services")

set(MSG_I_FLAGS "-Ioccupancy_grid_utils:/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/kinetic/share/sensor_msgs/cmake/../msg;-Inav_msgs:/opt/ros/kinetic/share/nav_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(occupancy_grid_utils_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg" NAME_WE)
add_custom_target(_occupancy_grid_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "occupancy_grid_utils" "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg" "nav_msgs/MapMetaData:geometry_msgs/Pose:geometry_msgs/Point:geometry_msgs/Quaternion"
)

get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg" NAME_WE)
add_custom_target(_occupancy_grid_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "occupancy_grid_utils" "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg" "sensor_msgs/PointCloud:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Point32:geometry_msgs/Point:geometry_msgs/Pose:sensor_msgs/ChannelFloat32"
)

get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg" NAME_WE)
add_custom_target(_occupancy_grid_utils_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "occupancy_grid_utils" "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg" "nav_msgs/MapMetaData:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Point:nav_msgs/OccupancyGrid:geometry_msgs/Pose"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_cpp(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/PointCloud.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point32.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/ChannelFloat32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_cpp(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/occupancy_grid_utils
)

### Generating Services

### Generating Module File
_generate_module_cpp(occupancy_grid_utils
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/occupancy_grid_utils
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(occupancy_grid_utils_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(occupancy_grid_utils_generate_messages occupancy_grid_utils_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_cpp _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_cpp _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_cpp _occupancy_grid_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(occupancy_grid_utils_gencpp)
add_dependencies(occupancy_grid_utils_gencpp occupancy_grid_utils_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS occupancy_grid_utils_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_eus(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/PointCloud.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point32.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/ChannelFloat32.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_eus(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/occupancy_grid_utils
)

### Generating Services

### Generating Module File
_generate_module_eus(occupancy_grid_utils
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/occupancy_grid_utils
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(occupancy_grid_utils_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(occupancy_grid_utils_generate_messages occupancy_grid_utils_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_eus _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_eus _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_eus _occupancy_grid_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(occupancy_grid_utils_geneus)
add_dependencies(occupancy_grid_utils_geneus occupancy_grid_utils_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS occupancy_grid_utils_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_lisp(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/PointCloud.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point32.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/ChannelFloat32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_lisp(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/occupancy_grid_utils
)

### Generating Services

### Generating Module File
_generate_module_lisp(occupancy_grid_utils
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/occupancy_grid_utils
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(occupancy_grid_utils_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(occupancy_grid_utils_generate_messages occupancy_grid_utils_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_lisp _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_lisp _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_lisp _occupancy_grid_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(occupancy_grid_utils_genlisp)
add_dependencies(occupancy_grid_utils_genlisp occupancy_grid_utils_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS occupancy_grid_utils_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_nodejs(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/PointCloud.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point32.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/ChannelFloat32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_nodejs(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/occupancy_grid_utils
)

### Generating Services

### Generating Module File
_generate_module_nodejs(occupancy_grid_utils
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/occupancy_grid_utils
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(occupancy_grid_utils_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(occupancy_grid_utils_generate_messages occupancy_grid_utils_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_nodejs _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_nodejs _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_nodejs _occupancy_grid_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(occupancy_grid_utils_gennodejs)
add_dependencies(occupancy_grid_utils_gennodejs occupancy_grid_utils_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS occupancy_grid_utils_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_py(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/PointCloud.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point32.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/sensor_msgs/cmake/../msg/ChannelFloat32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/occupancy_grid_utils
)
_generate_msg_py(occupancy_grid_utils
  "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/occupancy_grid_utils
)

### Generating Services

### Generating Module File
_generate_module_py(occupancy_grid_utils
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/occupancy_grid_utils
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(occupancy_grid_utils_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(occupancy_grid_utils_generate_messages occupancy_grid_utils_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/NavigationFunction.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_py _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/LocalizedCloud.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_py _occupancy_grid_utils_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/occupancy_grid_utils/msg/OverlayClouds.msg" NAME_WE)
add_dependencies(occupancy_grid_utils_generate_messages_py _occupancy_grid_utils_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(occupancy_grid_utils_genpy)
add_dependencies(occupancy_grid_utils_genpy occupancy_grid_utils_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS occupancy_grid_utils_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/occupancy_grid_utils)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/occupancy_grid_utils
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(occupancy_grid_utils_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(occupancy_grid_utils_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()
if(TARGET nav_msgs_generate_messages_cpp)
  add_dependencies(occupancy_grid_utils_generate_messages_cpp nav_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/occupancy_grid_utils)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/occupancy_grid_utils
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(occupancy_grid_utils_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(occupancy_grid_utils_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()
if(TARGET nav_msgs_generate_messages_eus)
  add_dependencies(occupancy_grid_utils_generate_messages_eus nav_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/occupancy_grid_utils)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/occupancy_grid_utils
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(occupancy_grid_utils_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(occupancy_grid_utils_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()
if(TARGET nav_msgs_generate_messages_lisp)
  add_dependencies(occupancy_grid_utils_generate_messages_lisp nav_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/occupancy_grid_utils)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/occupancy_grid_utils
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(occupancy_grid_utils_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(occupancy_grid_utils_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()
if(TARGET nav_msgs_generate_messages_nodejs)
  add_dependencies(occupancy_grid_utils_generate_messages_nodejs nav_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/occupancy_grid_utils)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/occupancy_grid_utils\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/occupancy_grid_utils
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(occupancy_grid_utils_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(occupancy_grid_utils_generate_messages_py sensor_msgs_generate_messages_py)
endif()
if(TARGET nav_msgs_generate_messages_py)
  add_dependencies(occupancy_grid_utils_generate_messages_py nav_msgs_generate_messages_py)
endif()
