# Install script for directory: /home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/navigation/goal_provider

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/build/navigation/goal_provider/catkin_generated/installspace/goal_provider.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/goal_provider/cmake" TYPE FILE FILES
    "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/build/navigation/goal_provider/catkin_generated/installspace/goal_providerConfig.cmake"
    "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/build/navigation/goal_provider/catkin_generated/installspace/goal_providerConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/goal_provider" TYPE FILE FILES "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/navigation/goal_provider/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/goal_provider" TYPE PROGRAM FILES "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/build/navigation/goal_provider/catkin_generated/installspace/goalSaver.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/goal_provider" TYPE PROGRAM FILES "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/build/navigation/goal_provider/catkin_generated/installspace/goalProvider.py")
endif()

