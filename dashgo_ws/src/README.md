# Multirobot simulation [WIP]

Development of multirobot simulation in RVIZ.

## How to run demo:

1. Modify the global [Multirobots launch file](https://github.com/RoBorregos/EAIBotSmartFactory/blob/navigation/multipleRoBotNav/dashgo_ws/src/navigation/launch/multiple_robots.launch) according to how many robots you want on the simulation.

2. Run the following command inside the __/dashgo_ws__:

   SSH:

   ```bash
   $ roslaunch src/navigation/launch/multiple_robots.launch
   ```

3. Run the small script to send a goal:

   ```bash
   $ rosrun goal_provider goalProvider.py
   ```
Use `Ctrl + C` in terminals to exit the logs and turn all nodes and application down.


### TODOs:

- Finish goal provider to automatize the sending of several goals.
- Create user app that integrates simulation control.
  - Visiualization of goals, robots and other information.
  - Control of environment
  - General system feedback
- Investigate how to launch it on Gazebo

