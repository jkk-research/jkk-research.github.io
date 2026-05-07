## `ROS 2` install hands-on workshop :simple-ros:{ .sze-color } 

This document will guide you through the installation process of `ROS 2`.

This document also served as small overview of the `Bavarian-Hungarian Self-driving vehicles` workshop.



## Install `ROS 2` video

[![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/DIYktkx3XLM?si=loa8CQQRUQFfFfuQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



# Windows WSL2

**Windows Subsystem for Linux** is a compatibility layer for native running of Linux-based elements on Windows 10 or Windows 11-based systems. You should choose to use WSL if you do not want to install native Ubuntu (e.g. 18.04 / 22.04) on your computers.

Steps to install:

- Run as administrator, open a PowerShell window.
- Copy the command below. You hereby authorize the use of WSL.
``` bash
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
- Restart the computer by entering the letter `Y`. *(optional)*
- Open the Microsoft Store and search for Windows Subsystem for Linux Preview. Install it.
- Also search for Ubuntu 22.04 in the Microsoft Store and install **or** PowerShell (Admin):
``` bash
wsl --install -d Ubuntu-22.04
```
- For easier handling, it is worth installing the Windows Terminal program as well. Also search for Windows Terminal in the Microsoft Store and install it.
- Start the Windows Terminal program and open the settings with the Ctrl+, (Control and comma) key combination. Select Ubuntu 22.04 from the drop-down list of the Default Profile setting line.
- Restart the Windows Terminal. When starting for the first time, enter a user name and password of your choice.
- We recommend the VS Code editor to develop the solution. Install from: [code.visualstudio.com/download](https://code.visualstudio.com/download)
- Finally, install the VS Code Remote Development add-on to be available using WSL: [marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack](https://marketplace.visualstudio.com /items?itemName=ms-vscode-remote.vscode-remote-extensionpack)


## Installation (after you have Ubuntu)

!!! danger "ROS 2"
    ROS 1 versions are only discussed for historical reasons, ROS 2 is recommended for current developments.

`ROS 1` is basically supported on Linux systems, although there have been attempts for other operating systems as well. On the other hand, `ROS 2` already supports running on native Windows, Mac OS or other Real-Time operating systems. So basically there are four options:

1. Dual boot, native Linux installed alongside Windows (mostly Ubuntu) ✅ [description](https://sze-info.github.io/arj/telepites/ubuntu.html)
2. Windows WSL2, lightweight Linux virtual machine ✅ [description](https://sze-info.github.io/arj/telepites/win10.html)
3. Virtual machine for Windows 🟠
4. Windows build 🟠

We recommend the first two of these 4 options, but of course the others are not prohibited either. Dual boot provides an insight into the Linux world, which is useful knowledge for an engineer today. Care must be taken during installation, as a wrong setting causes data loss, so a backup is also recommended. WSL (Windows Subsystem for Linux) is a lightweight compatibility layer for running Linux-based components on Windows 10 or Windows 11-based systems. As you can see in the following figure, the Linux kernel can access the hardware elements (CPU, memory, GPU) just as easily as the Windows kernel. Compared to this, the virtual machine (option 3) is a much slower solution that uses more abstraction layers, and is recommended for those who either have a very modern, fast machine or have already installed such systems. The native Windows build (option 4) is a given in principle, but since the majority of the documentation is available for Linux, it will mean a lot of extra work.

Illustration of the first three options:

![wsl overview](https://sze-info.github.io/ajr/assets/images_common/wsl_overview01.svg)

The following description applies to Ubuntu 22.04 Jammy. *Note* that other versions are also supported, their installation and descriptions are available here: [docs.ros.org/en/humble/Installation/Alternatives.html](https://docs.ros.org/en/humble/Installation/Alternatives.html)

The following description is based on [docs.ros.org/en/humble/Installation.html](https://docs.ros.org/en/humble/Installation.html).


## Set language

!!! note
    This step can usually be skipped


Make sure you have a locale that supports UTF-8.

``` r
locale # Check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

check locale # settings
```

## Set resources
You need to add the ROS 2 apt repository to your system.

First, make sure the Ubuntu Universe repository is enabled.

``` r
sudo apt install software-properties-common
sudo add-apt-repository universe
```

Add ROS 2 GPG key with `apt`.

``` r
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

Next comes the addition of the container to the source list.

``` r
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

## Install ROS 2 packages

Update:

``` r
sudo apt update
```

ROS 2 packages are often built on updated Ubuntu systems. It is always recommended to make sure your system is up-to-date before installing new packages.
``` r
sudo apt upgrade
```

Desktop installation: Installation of ROS, RViz, demos, tutorials:
``` r
sudo apt install ros-humble-desktop
```

Development tools, compilers, and other tools for building ROS packages:
``` r
sudo apt install ros-dev-tools
```

## Source

Set up your environment by sourcing the following file:

``` r
source /opt/ros/humble/setup.bash
```

Tip: this can also be done in the `.bashrc` file `echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc`.

# Check installation

We check the correctness of the installation with the `ros2 topic list` command.

``` r
$ ros2 topic list

/parameter_events
/rosout
```

If everything is fine, the above two topics should appear. Then you can learn how to use simple example nodes: [docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools.html](https://docs.ros.org/en/humble/Tutorials/Beginner -CLI-Tools.html)

# Recommended settings after installation

## Console colors

By default, the console output is not colored, but it is advisable to set this with the `RCUTILS_COLORIZED_OUTPUT` environment variable (even written in `bashrc`). For example:

``` r
export RCUTILS_COLORIZED_OUTPUT=1
```

![RCUTILS_COLORIZED_OUTPUT](https://github-production-user-asset-6210df.s3.amazonaws.com/11504709/248783932-a71a5d37-d49b-4508-93db-2e74a3c24365.gif)

Details: [docs.ros.org/en/humble/Tutorials/Demos/Logging-and-logger-configuration.html#id14](https://docs.ros.org/en/humble/Tutorials/Demos/Logging- and-logger-configuration.html#id14)

## `colcon_cd`

It is also advisable to set the `colcon_cd` command so that you can quickly change your working directory to the directory of a package. As an example, the command `colcon_cd some_ros_package` can quickly jump to the directory `~/ros2_ws/src/some_ros_package`.

Details: [docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html#setup-colcon-cd](https://docs.ros.org/en/humble/Tutorials/ Beginner-Client-Libraries/Colcon-Tutorial.html#setup-colcon-cd)

# Home / laboratory room installation

In the lab, we run the [following `install_humble.sh`](https://github.com/sze-info/ajr/blob/main/docs/telepites/install_humble.sh) file (shell script) on each machine.

``` bash
wget https://raw.githubusercontent.com/sze-info/ajr/main/docs/telepites/install_humble.sh
```
``` bash
sudo chmod +x install_humble.sh
```

At home:
``` bash
./install_humble.sh
```
In the laboratory room (campus):
``` bash
./install_humble.sh campus
```

## Installing WSL and Importing the Snapshot

Installation walkthrough video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/yBLtg2c4yA4?si=PO7NefOrQJQV0tG8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The steps from the video in text form:

1. Download the WSL snapshot (backup file): [Download WSL snapshot :material-download: ~2.5 GB](https://laesze-my.sharepoint.com/:u:/g/personal/herno_sze_hu/EYxEY_oJa7ZEursLIBMZeZ4BWUvT_LbkHbOIsPToBgRxbg?download=1){ .md-button}
2. Extract the snapshot `.zip` >> `.tar`
3. In PowerShell (Admin), enable the WSL feature, then install WSL:
``` powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
``` powershell
wsl --install --no-distribution
```
4. In PowerShell, import the WSL snapshot file (tar):
``` powershell
wsl --import ajr1 .\ajr1\ .\ajr24a.tar
```
5. Install VS Code and the WSL extension:

![wsl03](https://sze-info.github.io/ajr/assets/images_common/wsl03.png)

!!! danger
    The `wsl -l -v` command lists the installed WSL versions. The `VERSION` column must show `2`, otherwise an outdated version of WSL has been installed. Example of correct output:
``` bash
    NAME            STATE           VERSION
    Ubuntu          Stopped         2
    Ubuntu-22.04    Stopped         2
    Ubuntu-24.04    Running         2
    ajr1            Stopped         2
```
    If `1` appears in the `VERSION` column, you can update the version with the `wsl --update` command.

### Additional recommended settings

In Windows Terminal, it is recommended to set the `Default Profile` to `ajr1`, so the program always starts with that profile. The `Open windows from previous session` setting can also be useful so that the program reopens in its most recent state (e.g., with multiple panes).

![wsl04](https://sze-info.github.io/ajr/assets/images_common/wsl04.png)

Panes can then be created with the `Alt`+`Shift`+`minus` or `Alt`+`Shift`+`plus` keyboard shortcuts. This divides the terminal window (`Split pane`) into multiple sections vertically or horizontally.

![wsl05](https://sze-info.github.io/ajr/assets/images_common/wsl05.png)

# Workspace reset

If we want to delete the entire `ros2_ws`, then clone and build it again (~5 minutes), we can do it with the following single long command:

``` bash
cd ~ ; rm ws_reset.sh; wget https://raw.githubusercontent.com/sze-info/ajr/main/docs/telepites/ws_reset.sh; sudo chmod +x ws_reset.sh; ./ws_reset.sh
```
