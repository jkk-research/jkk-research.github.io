`ROS 2` humble jeston docker

# Repo used
https://github.com/dusty-nv/jetson-containers/

# Our repos
- https://github.com/jkk-research/docker_ros2_images

## Commands

``` bash
sudo apt-get update && sudo apt-get install git python3-pip
```

``` bash
git clone --depth=1 https://github.com/dusty-nv/jetson-containers
```
``` bash
cd jetson-containers
```

``` bash
pip3 install -r requirements.txt
```

### Run

``` bash
sudo docker run --runtime nvidia -it --rm --network=host dustynv/ros:humble-desktop-l4t-r32.7.1
```
``` bash
sudo docker run --runtime nvidia -it --rm --network=host dustynv/ros:humble-ros-base-l4t-r35.3.1
```
### Mount dir

``` bash
sudo docker run --runtime nvidia -it --rm -v /home/nvidia/:/test_dir --network=host dustynv/ros:humble-desktop-l4t-r32.7.1 
```


https://hub.docker.com/r/dustynv/ros
