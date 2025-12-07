from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os
import subprocess

def generate_launch_description():
    subprocess.run(['sudo', 'chmod', '777', '/dev/ttyUSB0'])
    subprocess.run(['sudo', 'chmod', '777', '/dev/ttyUSB1'])
    share_sllidar = get_package_share_directory('sllidar_ros2')
    share_nav2 = get_package_share_directory('nav2_bringup')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(share_sllidar, 'launch', 'sllidar_a1_launch.py')
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(share_sllidar, 'launch', 'rplidar_cartographer.launch.py')
            )
        ),

        Node(
            package='imu_publisher',
            executable='imu_publisher',
            name='imu_publisher',
            output='screen'
        ),
        
        
        #IncludeLaunchDescription(
        #    PythonLaunchDescriptionSource(
        #        os.path.join(share_nav2, 'launch', 'bringup_launch.py')
        #    ),
        #    launch_arguments={'use_sim_time': 'false'}.items()
        #),
    ])
