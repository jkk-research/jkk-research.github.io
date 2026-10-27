# `ROS 2` DDS settings

## `~/.bashrc`

``` bash
export ROS_DOMAIN_ID=0
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
# export FASTRTPS_DEFAULT_PROFILES_FILE=/home/<user>/fastdds_profile.xml
export CYCLONEDDS_URI=/home/<user>/cyclone_profile.xml
```

## `cyclone_profile.xml` file
``` xml
<CycloneDDS xmlns="https://cdds.io/config" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://cdds.io/config https://raw.githubusercontent.com/eclipse-cyclonedds/cyclonedds/master/etc/cyclonedds.xsd">
    <Domain id="any">
         <General>
           <Interfaces>
              <NetworkInterface name="tun0"  multicast="false" />
           </Interfaces>
           <AllowMulticast>false</AllowMulticast>
           <EnableMulticastLoopback>false</EnableMulticastLoopback>
        </General>

        <Discovery>
            <Peers>
                <Peer address="10.8.0.10"/> <!-- lexus.opn -->
                <Peer address="10.8.0.11"/> <!-- teleopstation.opn -->
                <Peer address="10.8.0.12"/> <!-- nisssan -->
                <Peer address="10.8.0.15"/> <!-- lexus-bme.ovpn -->
                <Peer address="10.8.0.17"/> <!-- gamma-rover.ovpn -->
                <Peer address="10.8.0.18"/> <!-- gamma-station.ovpn -->
                <Peer address="10.8.0.1"/>
            </Peers>
            <ParticipantIndex>auto</ParticipantIndex>
        </Discovery>

       <Domain id="any">
         <SharedMemory>
            <Enable>true</Enable>
            <SubQueueCapacity>256</SubQueueCapacity>
            <SubHistoryRequest>16</SubHistoryRequest>
            <PubHistoryCapacity>16</PubHistoryCapacity>
            <LogLevel>info</LogLevel>
         </SharedMemory>
       </Domain>

        <!--
        <Tracing>
            <Verbosity>config</Verbosity>
            <OutputFile>stdout</OutputFile>
        </Tracing>
        -->
    </Domain>
</CycloneDDS>
```
## `cyclone_profile.xml` file for Autoware 
https://autowarefoundation.github.io/autoware-documentation/main/installation/additional-settings-for-developers/network-configuration/dds-settings/
```xml
<CycloneDDS xmlns="https://cdds.io/config" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://cdds.io/config https://raw.githubusercontent.com/eclipse-cyclonedds/cyclonedds/master/etc/cyclonedds.xsd">
<!-- https://github.com/szenergy/szenergy-public-resources/wiki/ROS-2-DDS -->
    <Domain Id="any">
         <General>
           <Interfaces>
              <NetworkInterface autodetermine="false" name="lo" priority="default" multicast="default" />
              <!-- <NetworkInterface name="tun0"  multicast="false" /> -->
           </Interfaces>
           <AllowMulticast>default</AllowMulticast>
           <MaxMessageSize>65500B</MaxMessageSize>
           <!-- <EnableMulticastLoopback>false</EnableMulticastLoopback> -->
        </General>

        <Internal>
        <SocketReceiveBufferSize min="10MB"/>
        <Watermarks>
            <WhcHigh>500kB</WhcHigh>
        </Watermarks>
        </Internal>

        <!-- <Discovery> -->
            <!-- <Peers> -->
                <!-- <Peer address="10.8.0.10"/> lexus.opn -->
                <!-- <Peer address="10.8.0.11"/> teleopstation.opn -->
                <!-- <Peer address="10.8.0.12"/> nisssan -->
                <!-- <Peer address="10.8.0.15"/> lexus-bme.ovpn -->
                <!-- <Peer address="10.8.0.17"/>  gamma-rover.ovpn -->
                <!-- <Peer address="10.8.0.18"/>  gamma-station.ovpn -->
                <!-- <Peer address="10.8.0.1"/> -->
            <!-- </Peers> -->
            <!-- <ParticipantIndex>auto</ParticipantIndex> -->
            <!-- <MaxAutoParticipantIndex>100</MaxAutoParticipantIndex> -->
        <!-- </Discovery> -->
        <!--
        <Tracing>
            <Verbosity>config</Verbosity>
            <OutputFile>stdout</OutputFile>
        </Tracing>
        -->
    </Domain>
</CycloneDDS>
```


## `fastdds_profile.xml` file

``` xml
<?xml version="1.0" encoding="UTF-8" ?>
<profiles xmlns="http://www.eprosima.com/XMLSchemas/fastRTPS_Profiles">
    <participant profile_name="initial_peers_profile" is_default_profile="true" >
        <rtps>
            <builtin>
                <initialPeersList>
                    <locator>
                        <udpv4>
                            <address>10.8.0.10</address> <!-- lexus.opn -->
                        </udpv4>
                        <udpv4>
                            <address>10.8.0.11</address> <!-- teleopstation.opn -->
                        </udpv4>
                        <udpv4>
                            <address>10.8.0.12</address> <!-- nissan -->
                        </udpv4>
                        <udpv4>
                            <address>10.8.0.15</address> <!-- lexus-bme.ovpn -->
                        </udpv4>
                        <udpv4>
                            <address>10.8.0.17</address> <!-- gamma-rover.ovpn -->
                        </udpv4>
                        <udpv4>
                            <address>10.8.0.18</address> <!-- gamma-station.ovpn -->
                        </udpv4>
                    </locator>
                </initialPeersList>
            </builtin>
        </rtps>
    </participant>
</profiles>
```

``` r
sudo apt install openvpn
```
``` r
/etc/default/openvpn  ## autostart
```

``` bash
sudo systemctl enable openvpn
```
``` bash
systemctl status openvpn
```
``` r
systemctl restart openvpn
```

``` bash
ros2 daemon status
```
``` bash
ros2 daemon start
```
``` bash
ros2 daemon stop
```
``` bash 
echo $RMW_IMPLEMENTATION
```
