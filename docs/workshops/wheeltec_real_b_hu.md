# Wheeltec `101`

- **Robot**: Wheeltec Roboworks Ackermann Mini  
- **ROS verzió**: ROS 2 Jazzy *(de működik ROS 2 Humble alatt is)*  

[![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)  
[![Static Badge](https://img.shields.io/badge/ROS_2-Jazzy-34aec5)](https://docs.ros.org/en/jazzy/)

![](/img/wheeltec_roboworks02.png)

Rövid link az oldalhoz: [go.sze.hu/wh](https://go.sze.hu/wh)

---

## `1.` Alap használat

### Robot csatlakozás

| tulajdonság | alapértelmezett |
|---|---|
|`user@hostname` | `wheeltec@roboworks` <br /> `wheeltec@192.168.0.1##` |
|SSID | `wheeltec_robo_##` |
|Jelszó | `dongguan` |

---

### Akkumulátor állapot

| állapot | feszültség |
|---|---|
|🟢 | 21.0 `V` – 25.0 `V` |
|🟡 | 20.0 `V` – 21.0 `V` |
|🔴 | < 20.0 `V` |

![](https://raw.githubusercontent.com/robotverseny/fyi/refs/heads/main/etc/wheetec_battery01.png)

---

### `nmtui` / WiFi hotspot

```yaml
Profile name: hotspot1
Device: wlan0
SSID: wheeltec_robo_#
Mode: Access Point
Security: WPA & WPA2 Personal
Password: dongguan
IPv4 address: from 192.168.0.101/24 to 192.168.0.113/24 
IPv4 gateway: 192.168.0.1
```

![](https://raw.githubusercontent.com/robotverseny/fyi/refs/heads/main/etc/nmtui01.png)

---

### VS Code SSH

```bash
ssh wheeltec@192.168.0.100
```

---

## `2.` ROS 2 használata

```bash
source ~/ros2_ws/install/setup.bash
```

```bash
start_drivers
```

```bash
stop_all
```

![](/img/start_wheeltec_driver01.png)

---

## `3.` Adatrögzítés

```bash
ros2 launch mcap_rec preset_wheeltec01.launch.py tag:=scenario01
```

---

## `4.` Vizualizáció

![](https://sze-info.github.io/ajr/assets/images_common/foxglove_lichtblick01.png)

![](https://raw.githubusercontent.com/robotverseny/megoldas_zala23/main/etc/rosbag_foxglove01.gif)

---

## `5.` Kód szerkesztése VS Code-ban

A roboton történő kódszerkesztés ajánlott módja a VS Code használata a  
[`Remote - SSH` bővítménnyel](https://code.visualstudio.com/docs/remote/ssh).

![](https://sze-info.github.io/ajr/assets/images_common/vscodebasics02.png)

![](https://code.visualstudio.com/assets/docs/remote/ssh/architecture-ssh.png)

---

## `6.` Parancsok

| Parancs | Leírás |
|---|---|
|`start_drivers` | A robot driverek indítása háttérben |
|`stop_all` | Minden háttérfolyamat leállítása (screen segítségével indítottak) |
|`r2` | ROS 2 workspace betöltése (ugyanaz, mint `source ~/ros2_ws/install/setup.bash`) |
|`ros2 topic list` | Az aktív topicok listázása |
|`ros2 topic echo /topic_name` | Egy topic üzeneteinek megjelenítése |
|`ros2 topic hz /topic_name` | Egy topic publikálási frekvenciája |
|`ros2 topic info /topic_name -v` | Részletes információ egy topicról |
|`ros2 node list` | Az aktív node-ok listázása |

---

## Hasznos linkek

- [go.sze.hu/wh](https://go.sze.hu/wh)
- [foxglove.dev](https://foxglove.dev/)
- [github.com/lichtblick-suite/lichtblick](https://github.com/lichtblick-suite/lichtblick)
- [github.com/robotverseny/fyi](https://github.com/robotverseny/fyi)
- [github.com/szenergy/szenergy-public-resources/wiki/H-SSH-no-password](https://github.com/szenergy/szenergy-public-resources/wiki/H-SSH-no-password)
- [github.com/robotverseny/jkk_utils/tree/mcap_rec/mcap_rec](https://github.com/robotverseny/jkk_utils/tree/mcap_rec/mcap_rec)
- [github.com/robotverseny/megoldas_sim24](https://github.com/robotverseny/megoldas_sim24)
- [jkk-research.github.io/workshops/f1tenth_sim_a](https://jkk-research.github.io/workshops/f1tenth_sim_a)
- [code.visualstudio.com/docs/remote/ssh](https://code.visualstudio.com/docs/remote/ssh)

---

![](/img/wheeltec_roboworks01.png)