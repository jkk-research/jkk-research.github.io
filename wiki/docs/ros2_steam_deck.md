ROS 2 + Valve Steam Deck

2 options:
- [Ubuntu dual boot](#1st-option-ubuntu-dual-boot)
- [Arch linux](#2nd-option-arch-linux)

<img width="1122" height="703" alt="image" src="https://github.com/user-attachments/assets/1aa39c15-72ac-4181-814d-fa968bbbc886" />


# 1st option: Ubuntu dual boot 

What is known to be working is `24.04`+`Jazzy`

## Install
```bash
sudo apt install ros-jazzy-joy ros-jazzy-teleop-twist-joy
```
```bash
deck@u24:~$ ls /dev/input/by-id/
usb-17ef_Lenovo_USB_Receiver-event-if02
usb-17ef_Lenovo_USB_Receiver-event-kbd
usb-17ef_Lenovo_USB_Receiver-if01-event-mouse
usb-17ef_Lenovo_USB_Receiver-if01-mouse
usb-Valve_Software_Steam_Deck_Controller_MEDA33302CF4-event-if02
usb-Valve_Software_Steam_Deck_Controller_MEDA33302CF4-event-kbd
usb-Valve_Software_Steam_Deck_Controller_MEDA33302CF4-if01-event-mouse
usb-Valve_Software_Steam_Deck_Controller_MEDA33302CF4-if01-mouse
usb-Valve_Software_Steam_Deck_Controller_MEDA33302CF4-if02-event-joystick
usb-Valve_Software_Steam_Deck_Controller_MEDA33302CF4-if02-joystick
```

## Run

```bash
ros2 run joy joy_node --ros-args -p dev:=/dev/input/by-id/usb-Valve_Software_Steam_Deck_Controller_MEDA33302CF4-if02-event-joystick
```
or with autorepeat

```bash
ros2 run joy joy_node --ros-args -p dev:=/dev/input/by-id/usb-Valve_Software_Steam_Deck_Controller_MEDA33302CF4-if02-event-joystick -p deadzone:=0.1 -p autorepeat_rate:=20.0
```

<img width="752" height="465" alt="image" src="https://github.com/user-attachments/assets/07b51779-d734-4d38-8cfd-9750a4d2e9b6" />


Further: [github.com/jkk-research/jkk_utils/tree/ros2/steam_deck_jkk](https://github.com/jkk-research/jkk_utils/tree/ros2/steam_deck_jkk)

todo

# 2nd option: Arch linux

[pixi.prefix.dev/latest/tutorials/ros2/](https://pixi.prefix.dev/latest/tutorials/ros2/)

todo


# Further

todo
<img src="https://raw.githubusercontent.com/jkk-research/jkk_utils/refs/heads/ros2/steam_deck_jkk/img/steamdeck01.svg" alt="Steam Deck" width="400"/>

