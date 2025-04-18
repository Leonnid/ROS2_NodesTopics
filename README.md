
# ROS2 Setup and Execution

## Setup Environment
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

## Setup Environment
```bash
source /opt/ros/humble/setup.bash
```

## Create Package
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python my_robot_pkg
```

## Build Package
```bash
cd ~/ros2_ws
colcon build --packages-select my_robot_pkg
source install/setup.bash
```

## Run Nodes
```bash
ros2 run my_robot_pkg multi_publisher
ros2 run my_robot_pkg multi_subscriber
```

## Publish to Topic
```bash
ros2 topic pub /temperature std_msgs/msg/Float32 "{data: 25.5}"
```
