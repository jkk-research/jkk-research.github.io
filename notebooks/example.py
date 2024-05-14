# Reading from a MCAP file
# sudo apt install ros-$ROS_DISTRO-ros-base ros-$ROS_DISTRO-ros2bag ros-$ROS_DISTRO-rosbag2-transport ros-$ROS_DISTRO-rosbag2-storage-mcap 
import matplotlib.pyplot as plt
from mcap import __version__
print(__version__)


"""script that reads ROS2 messages from an MCAP bag using the rosbag2_py API."""
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message
import rosbag2_py


def read_messages(input_bag: str):
    reader = rosbag2_py.SequentialReader()
    reader.open(rosbag2_py.StorageOptions(uri=input_bag, storage_id="mcap"), rosbag2_py.ConverterOptions(input_serialization_format="cdr", output_serialization_format="cdr" ),)

    topic_types = reader.get_all_topics_and_types()

    def typename(topic_name):
        for topic_type in topic_types:
            if topic_type.name == topic_name:
                return topic_type.type
        raise ValueError(f"topic {topic_name} not in bag")

    while reader.has_next():
        topic, data, timestamp = reader.read_next()
        msg_type = get_message(typename(topic))
        msg = deserialize_message(data, msg_type)
        yield topic, msg, timestamp
    del reader

inputs = []

# list all *.mcap in /mnt/c/bag/ 
directory = "/mnt/c/bag/jkkds02/"
import os
for filename in os.listdir(directory):
    if filename.endswith(".mcap"):
        #print(os.path.join(directory, filename))
        inputs.append(os.path.join(directory, filename))
    else:
        continue






i = 0
first_run = True
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

for input in inputs:
    print(input)
    plt.title('Vehicle Odometry\n' + input)
    x = []
    y = []
    for topic, msg, timestamp in read_messages(input):
        if(first_run):
            timestamp_start = timestamp
            first_run = False
        if (i % 1 == 0): # resample if necessary, 1 is no resampling
            if(topic == "/nissan/vehicle_speed"):
                speed_data = msg.data
                speed_time = (timestamp-timestamp_start) / 1000000000
            if(topic == "/nissan/gps/duro/current_pose"):
                x.append(msg.pose.position.x)
                y.append(msg.pose.position.y)
    plt.plot(x, y, label=input)



plt.legend()
plt.show()