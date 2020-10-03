# mobile_robot_description
ROS Package with a modular structure to create mobile robots with differential drive configuration. This package has some modules that can be parametrized using YAML files, making it easier, fast, and more flexible to create your robot model.

- [Package Organization](##PackageOrganization)
- [Installation](##Installation)

## Package Organization
This project has the following folder structure.

- **config:** Folder to place the config files with the parameters of the parts of the robot and also some config files to the RVIZ.
    - *sub-folder:* The config files to a specific project should be placed in a sub-folder in order to make possible have different models in the same project.
- **launch:** Folder with the launch files for the robots.
- **meshes:** Folder to place the mesh files for the links of the robot. These meshes files will be used **only** as visual. The collision of the links is set as basic shapes to reduce the computational cost as the Gazebo tutorial suggests.
    - *sub-folder:* The specific mesh files of each project should be placed in the sub-folder with the name of the project.
- **rviz:** Folder with the RVIZ configuration for the robot.
- **urdf:** Folder with the URDF and xacro files.
    - ***include:*** Folder with the common module files, similar to the Libs.

## Installation
To install this package, just clone it inside your ROS workspace, running:

``` 
$ git clone https://github.com/pxalcantara/mobile_robot_description.git 
```

