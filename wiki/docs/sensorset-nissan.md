---
title: Nissan Leaf Sensorset 
# permalink: /wiki/2026.L/
icon: material/car
---



Vehicle: Nissan Leaf 1.gen

<figure markdown="span">
  ![Image](https://jkk-research.github.io/latest/assets/images_common/vehcile_leaf01.png){ width="80%" }
  <figcaption>Nissan Leaf</figcaption>
</figure>

Sensors:

|Type|Name|Pieces| ROS2 driver |
|---|---|---|---|
|LIDAR|Ouster OS1-64|1|[ouster-ros](https://github.com/ouster-lidar/ouster-ros)|
|Camera| TierIV C2|1|[usb-cam](https://github.com/ros-drivers/usb_cam)
|GPS|Novatel PwrPak7 Dual GNSS Antenna|1| [novatel_oem7_driver](https://github.com/novatel/novatel_oem7_driver) |
|GPS| SwiftNav Duro |1| [duro_gps_driver](https://github.com/szenergy/duro_gps_driver) |
|GPS| Fixposition Vision-RTK 2|1| [fixposition_ros_driver](https://github.com/fixposition/fixposition_driver)|

IP addresses:

|IP address|Device|
|---|---|
|`192.168.11.1`|ZTE router|
|`192.168.11.2`|MikroTik switch|
|`192.168.11.5`|Neousys|
|`192.168.11.22`|NI cRIO|
|`192.168.11.108`|Ouster|
|`192.168.11.110`|Novatel|
|`192.168.11.112`|Duro|
|`192.168.11.124`|Fixposition|


<iframe width="560" height="315" src="https://www.youtube.com/embed/9eFqsei1J70?si=Y9rnsmGnoiofxhiz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>