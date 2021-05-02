#!/usr/bin/env python3
#
# Copyright 2020 Open BR
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import xacro


def generate_launch_description():

    # Get dir names
    pkg_share = get_package_share_directory('mobile_robot_description')
    # pkg_share = get_package_share_directory('diffbot2_description')

    # Get rviz config
    rviz_config = PathJoinSubstitution([
        FindPackageShare('mobile_robot_description'), 'rviz/view_robot.rviz'
    ])

    # Add launch description variables
    namespace = LaunchConfiguration('namespace')
    spawn_robot = LaunchConfiguration('spawn_robot')
    # robot_description = LaunchConfiguration('robot_description')

    # Add launch arguments
    namespace_arg = DeclareLaunchArgument(
                        name='namespace',
                        default_value='',
                        description='Node namespace')

    spawn_robot_arg = DeclareLaunchArgument(
                    name='spawn_robot',
                    default_value='false',
                    description='Flag to spawn the robot or not')

    # Compute robot_description string
    xacro_file = os.path.join(pkg_share, 'urdf/mobile_robot.urdf.xacro')
    robot_description = xacro.process(xacro_file)

    # Define parameters
    common_params = {
        'robot_description': robot_description,
    }

    # Add nodes
    robot_state_publisher = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            namespace=namespace,
            parameters=[common_params])

    joint_state_publisher = Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            namespace=namespace,
            parameters=[common_params])

    rviz_node = Node(
            condition=IfCondition(spawn_robot),
            package='rviz2',
            executable='rviz2',
            name='rviz',
            output='screen',
            namespace=namespace,
            arguments=['-d', rviz_config])

    # Launch description
    launch_description = LaunchDescription()

    # Add launch actions to the launch description
    launch_description.add_action(namespace_arg)
    launch_description.add_action(spawn_robot_arg)
    launch_description.add_action(robot_state_publisher)
    launch_description.add_action(joint_state_publisher)
    launch_description.add_action(rviz_node)

    return launch_description
