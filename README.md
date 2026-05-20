<img width="960" height="504" alt="gazebo" src="https://github.com/user-attachments/assets/54d663a6-e164-4bef-8854-d3e6a2feb9e6" /># ros2-r2d2-sim

An R2D2-inspired differential drive robot built with ROS2, URDF, Gazebo, and RViz2 — my first hands-on project for learning robot modeling, TF trees, and the ROS2 simulation pipeline end-to-end.

---

## Overview

This project started as a way to understand how ROS2 packages are structured and how robot models move through the URDF → `robot_state_publisher` → TF → RViz2/Gazebo pipeline. The robot is modeled after R2D2 using primitive URDF shapes (cylinders and boxes), making it easy to follow and extend.

### What this project covers

* Authoring a multi-link URDF with fixed and continuous joints
* Publishing joint states and TF frames via `robot_state_publisher`
* Visualizing the robot model and TF tree in RViz2
* Spawning and simulating the robot in Gazebo
* Writing a basic ROS2 node to publish velocity commands (`/cmd_vel`)

---

## Screenshots

| Gazebo                                     | RViz2                                 |
| ------------------------------------------ | ------------------------------------- |
| <img width="960" height="504" alt="gazebo" src="https://github.com/user-attachments/assets/e703f2cf-65a3-45d4-a462-9bb84f803ad8" />
 | <img width="960" height="540" alt="rviz" src="https://github.com/user-attachments/assets/f4a59508-0c19-40cc-8ef6-fd373f53ecbc" />
 |

---

## Project Structure

```bash
my_package/
├── launch/
│   ├── demo.launch.py
│   └── view.launch.py
├── urdf/
│   └── my_robot.urdf
├── docs/
│   ├── gazebo.png
│   └── rviz.png
├── my_package/
│   ├── move_robot.py
│   ├── listener.py
│   └── __init__.py
├── package.xml
├── setup.py
└── README.md
```

---

## Dependencies

* ROS2 Humble
* Gazebo Classic
* robot_state_publisher
* joint_state_publisher_gui
* rviz2
* gazebo_ros_pkgs

Install dependencies:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

---

## Build & Run

### Clone and build

```bash
cd ~/ros2_ws/src
git clone https://github.com/<your-username>/ros2-r2d2-sim.git

cd ~/ros2_ws

colcon build --packages-select my_package

source install/setup.bash
```

---

### Launch RViz2 visualization

```bash
ros2 launch my_package view.launch.py
```

---

### Launch Gazebo simulation

```bash
ros2 launch my_package demo.launch.py
```

---

### Drive the robot

Open another terminal:

```bash
source install/setup.bash

ros2 run my_package move_robot
```

---

## Key Concepts Practiced

| Concept                    | File / Usage                   |
| -------------------------- | ------------------------------ |
| URDF modeling              | `urdf/my_robot.urdf`           |
| TF publishing              | `robot_state_publisher`        |
| Joint visualization        | `joint_state_publisher_gui`    |
| Gazebo spawning            | `demo.launch.py`               |
| ROS2 topics                | `/cmd_vel`                     |
| Publisher/subscriber nodes | `move_robot.py`, `listener.py` |

---

## What I Learned

* How URDF links and joints map into TF frames
* How RViz2 and Gazebo use the same robot description differently
* How launch files simplify running multiple ROS2 nodes together
* Basic ROS2 publisher/subscriber communication
* Robot visualization and simulation workflow in ROS2

---

## Next Steps

* [ ] Convert the URDF into Xacro
* [ ] Add ros2_control support
* [ ] Create a custom Gazebo world
* [ ] Add keyboard teleoperation
* [ ] Improve robot movement logic


