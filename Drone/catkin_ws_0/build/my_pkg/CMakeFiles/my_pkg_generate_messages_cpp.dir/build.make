# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/dron/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/dron/catkin_ws/build

# Utility rule file for my_pkg_generate_messages_cpp.

# Include the progress variables for this target.
include my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/progress.make

my_pkg/CMakeFiles/my_pkg_generate_messages_cpp: /home/dron/catkin_ws/devel/include/my_pkg/AddTwoInts.h


/home/dron/catkin_ws/devel/include/my_pkg/AddTwoInts.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/dron/catkin_ws/devel/include/my_pkg/AddTwoInts.h: /home/dron/catkin_ws/src/my_pkg/srv/AddTwoInts.srv
/home/dron/catkin_ws/devel/include/my_pkg/AddTwoInts.h: /opt/ros/melodic/share/gencpp/msg.h.template
/home/dron/catkin_ws/devel/include/my_pkg/AddTwoInts.h: /opt/ros/melodic/share/gencpp/srv.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/dron/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating C++ code from my_pkg/AddTwoInts.srv"
	cd /home/dron/catkin_ws/src/my_pkg && /home/dron/catkin_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/dron/catkin_ws/src/my_pkg/srv/AddTwoInts.srv -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -p my_pkg -o /home/dron/catkin_ws/devel/include/my_pkg -e /opt/ros/melodic/share/gencpp/cmake/..

my_pkg_generate_messages_cpp: my_pkg/CMakeFiles/my_pkg_generate_messages_cpp
my_pkg_generate_messages_cpp: /home/dron/catkin_ws/devel/include/my_pkg/AddTwoInts.h
my_pkg_generate_messages_cpp: my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/build.make

.PHONY : my_pkg_generate_messages_cpp

# Rule to build all files generated by this target.
my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/build: my_pkg_generate_messages_cpp

.PHONY : my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/build

my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/clean:
	cd /home/dron/catkin_ws/build/my_pkg && $(CMAKE_COMMAND) -P CMakeFiles/my_pkg_generate_messages_cpp.dir/cmake_clean.cmake
.PHONY : my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/clean

my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/depend:
	cd /home/dron/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/dron/catkin_ws/src /home/dron/catkin_ws/src/my_pkg /home/dron/catkin_ws/build /home/dron/catkin_ws/build/my_pkg /home/dron/catkin_ws/build/my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : my_pkg/CMakeFiles/my_pkg_generate_messages_cpp.dir/depend

