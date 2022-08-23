"""Launch the hokuyo3d node."""

import os

import yaml
from ament_index_python import packages
from launch_ros.actions import Node

import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    ld = launch.LaunchDescription()
    share_dir = packages.get_package_share_directory("hokuyo3d")
    params_file = LaunchConfiguration("params_file")
    declare_params_file_cmd = DeclareLaunchArgument(
        "params_file",
        default_value=os.path.join(share_dir, "config", "hokuyo3d_params.yaml"),
        description="Params file for the hokuyo3d node",
    )
    hokuyo3d_node = Node(
        package="hokuyo3d",
        executable="hokuyo3d",
        output="screen",
        # prefix=['xterm -e gdb -ex run --args'],
        prefix=['gdbserver localhost:3000'],
        emulate_tty=True,
        parameters=[params_file],
    )

    ld.add_action(declare_params_file_cmd)
    ld.add_action(hokuyo3d_node)
    return ld
