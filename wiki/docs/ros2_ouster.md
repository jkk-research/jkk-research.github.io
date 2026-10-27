---
title: Ouster ROS 2 driver
---

# Ouster ROS 2 driver

This page is a practical quick start for the official Ouster ROS 2 driver from [ouster-lidar/ouster-ros](https://github.com/ouster-lidar/ouster-ros). It focuses on the workflow we use most often: prepare a ROS 2 workspace, build the driver, and launch a live sensor.

For hardware background and model comparison, see the general Ouster overview in [ouster.md](ouster.md).

## What the driver does

The ROS 2 driver connects to an Ouster sensor, configures it, and publishes the live data as ROS topics. The main outputs are:

- `/ouster/imu`
- `/ouster/points`
- `/ouster/points2` when the sensor is configured for dual return

## Before you start

The official ROS 2 branch targets Rolling, Humble, Iron, Jazzy, and Kilted. In practice, you should already have a working ROS 2 installation and a sourced workspace environment.

Install the common dependencies first:

```bash
sudo apt update
sudo apt install -y \
	build-essential \
	cmake \
	libeigen3-dev \
	libjsoncpp-dev \
	libspdlog-dev \
	libcurl4-openssl-dev \
	python3-colcon-common-extensions \
	ros-$ROS_DISTRO-pcl-ros \
	ros-$ROS_DISTRO-tf2-eigen \
	ros-$ROS_DISTRO-rviz2
```

If you plan to use PCAP replay later, also install `libpcap-dev`.

## Clone and build

Create a ROS 2 workspace and clone the ROS 2 branch of the driver into `src`:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone -b ros2 --recurse-submodules https://github.com/ouster-lidar/ouster-ros.git
```

Source your ROS 2 environment and build the workspace with `colcon`:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
cd ~/ros2_ws
colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release
```
We currently use the `lexus_bringup` repository.

To launch all sensors and generate a merged point cloud, run:

```bash
ros2 launch lexus_bringup lidar_os_merged.launch.py
```

The sensor configuration files are located in `lexus_bringup/config/lidar`.

The Ouster sensor IP addresses are:

- Ouster Center: `192.168.10.20`
- Ouster Left: `192.168.10.23`
- Ouster Right: `192.168.10.21`