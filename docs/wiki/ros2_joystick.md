# Easy way

> [!Caution]  
> Foxglove extension is the **easy** way.

Download `foxe` extension file for Foxglove Studio, drag and drop `foxglove-joystick` extension.

- [github.com/joshnewans/foxglove-joystick/releases](https://github.com/joshnewans/foxglove-joystick/releases)
- [github.com/joshnewans/foxglove-joystick](https://github.com/joshnewans/foxglove-joystick)

![](https://sze-info.github.io/ajr/onallo/joy1.gif)


# Alternative way

> [!IMPORTANT]  
> Reboot is needed during the process 2X

## Original description
This description only works with `--force` option, which is not included:
[learn.microsoft.com/en-us/windows/wsl/connect-usb](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)

ROS specific stuff are written here:


## Powershell (admin)


```powershell
winget install --interactive --exact dorssel.usbipd-win
```

```powershell
PS C:\Users\he> usbipd list
Connected:
BUSID  VID:PID    DEVICE                                                        STATE
1-3    1c4f:00b0  USB Input Device                                              Not shared
1-7    046d:c21d  Xbox 360 Controller for Windows                               Not shared
1-9    17ef:608c  USB Input Device                                              Not shared

Persisted:
GUID                                  DEVICE
```


Use `-f` or `--force`:
```powershell
usbipd bind --busid 1-7 -f
```

```powershell
PS C:\Users\he> usbipd list
Connected:
BUSID  VID:PID    DEVICE                                                        STATE
1-3    1c4f:00b0  USB Input Device                                              Not shared
1-7    046d:c21d  Xbox 360 Controller for Windows                               Shared (forced)
1-9    17ef:608c  USB Input Device                                              Not shared

Persisted:
GUID                                  DEVICE
```

## Go to WSL

```powershell
he@JKK46:~$ lsusb
 Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
 Bus 001 Device 002: ID 046d:c21d Logitech, Inc. F310 Gamepad [XInput Mode]
 Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

he@JKK46:~$ ls -l /dev/bus/usb/001/002
 crw-rw-r-- 1 root root 189, 1 Sep 20 08:53 /dev/bus/usb/001/002
```

Add `-a` for automatic mount to WSL.

```powershell
PS C:\Users\he> usbipd attach --wsl --busid 1-7 -a
usbipd: info: Using WSL distribution 'Ubuntu' to attach; the device will be available in all WSL 2 distributions.
usbipd: info: Using IP address 172.17.80.1 to reach the host.
```

```powershell
sudo chmod a+rw /dev/bus/usb/001/002
```

```powershell
sudo apt install ros-humble-joy
```

```powershell
ros2 run joy joy_node --ros-args -p device_name:=/dev/bus/usb/001/002
```

![](https://raw.githubusercontent.com/szenergy/szenergy-utility-programs/refs/heads/master/udp_joystick_ros/img/joy01.svg)