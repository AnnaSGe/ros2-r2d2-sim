from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command

def generate_launch_description():

    urdf_path = '/home/annas/ros2_ws/src/my_package/urdf/my_robot.xacro'

    robot_desc = Command(['xacro', ' ', urdf_path])

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
        ),

        Node(
            package='my_package',
            executable='move_robot'
        ),

    ])