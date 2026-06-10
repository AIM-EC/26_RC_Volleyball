from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config_file = os.path.join(
        get_package_share_directory('soem_bringup'),
        'config',
        'config-vol.yaml'
    )

    return LaunchDescription([
        Node(
            package='soem_wrapper',
            executable='soem_backend',
            name='soem_backend',
            parameters=[{
                'interface': "enp2s0",
                'rt_cpu': 4,
                'non_rt_cpus': "0-3,5-11",
                'config_file': config_file
            }],
            output='screen'
        )
    ])