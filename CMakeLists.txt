cmake_minimum_required(VERSION 3.5)
project(mobile_robot_description)

find_package(ament_cmake REQUIRED)

# Auto lint
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # find_package(launch_testing_ament_cmake REQUIRED)

  ament_lint_auto_find_test_dependencies()
  # add_launch_test(test/spawn_robot.test.py)
endif()

# Install share files
install(DIRECTORY 
  launch 
  urdf
  config
  rviz
  meshes
  DESTINATION share/${PROJECT_NAME}
  # PATTERN "view_robot.launch.py" EXCLUDE
)

ament_package()
