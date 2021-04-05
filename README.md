# EAIBot Smart Factory               


Development of an automated robotic warehouse simulationj system that retrieves, classifies and stores materials and products. Some tech areas involved include safety, object and person recognition, object manipulation, robot-robot communication/coordination and robot-human interaction/cooperation.

## Table of contents

- [EAIBot Smart Factory](#eaibot-smart-factory)
  - [Table of contents](#table-of-contents)
  - [Project details](#project-details)
  - [Project setup](#project-setup)
    - [Running project](#running-nav-simulation)
  - [Development team](#development-team)

## Project Details

This project is made using [EAIBot Dashgo B1](http://www.eaibot.com/product/B1) platform, wich runs with [ROS Kinetic](http://wiki.ros.org/kinetic).

For more information about project management and standards you can check our [wiki](https://github.com/RoBorregos/roborregos-web/wiki).


## Project setup

Before setting up the project, you should have installed the following development tools:

- [ROS Kinetic](http://wiki.ros.org/kinetic/Installation)

Once you have installed the required third-party software, you can follow this steps:

1. Clone the project repository on your local machine.

   SSH:

   ```bash
   $ git clone --recurse-submodules https://github.com/RoBorregos/smart-factory.git
   ```

2. Enter __/dashgo_ws__ and install all dependencies using rosdep:

   ```bash
   $ rosdep install --from-paths . --ignore-src --rosdistro=kinetic
   ```

### Running nav simulation

To build ROS packages, run inside the __/dashgo_ws__:

```bash
$ catkin_make
```

Source the code:

```bash
$ source devel/setup.bash
```

And run simulation:

```bash
$ roslaunch src/navigation/launch/nav_simul.launch 
```

For mock odometry movement also launch __move_base__ node:

```bash
$ roslaunch src/navigation/launch/nav_simul.launch 
```

Use `Ctrl + C` to exit the logs and turn all nodes and application down.

## Development team

| Name                    | Email                                                               | Github                                                       | Role      |
| ----------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------ | --------- |
| Aurora Tijerina | [auro.tj@gmail.com](mailto:auro.tj@gmail.com)                       | [@AuroTB](https://github.com/aurotb)                         | PM & navigation |
| Iqui Balam  | [iquibalamhm@gmail.com](mailto:iquibalamhm@gmail.com) | [@IquiBalamHM ](https://github.com/IquiBalamHM ) | Computer vision |
| Paul Vazquez | [pev@live.com.mx](mailto:pev@live.com.mx) | [@paulvazbad](https://github.com/paulvazbad) | Robot sinchronization and system coordination |
| Miguel Elizondo | [pev@live.com.mx](mailto:pev@live.com.mx) | [@Miguelelizondov](https://github.com/Miguelelizondov) | Cobot arm control |
