# TIER IV C2 Camera Datasheet (Short)

![TIER IV C2](https://tier4.github.io/edge-auto-docs/_images/c2_header.jpg)

## Visuals

![C2 block diagram](https://tier4.github.io/edge-auto-docs/_images/C2_block_diagram.drawio.png)

![C2 synchronization timing](https://tier4.github.io/edge-auto-docs/_images/c2_sync_1.png)

![C2 mechanical outline (120 deg)](https://tier4.github.io/edge-auto-docs/_images/c2_outline_120.png)

| Parameter | Specification |
|---|---|
| Image sensor | Sony IMX490, 1/1.55 in optical format, 3.0 um pixel |
| Effective resolution | 2880 x 1860 (5.4 MP) |
| Dynamic range | 120 dB equivalent HDR |
| LED flicker mitigation | Supported |
| Output interface | GMSL2 |
| Output format | YUV422, 8-bit, 16-bit/pixel |
| Max frame rate | 30 fps |
| Shutter | Rolling shutter (fixed) |
| Serializer | Analog Devices MAX9295A |
| ISP | Indie Semiconductor GW5300 |
| Drive modes | Master mode, Trigger mode (FSYNC) |
| Synchronization | Trigger input over GMSL (sensor readout aligned to FSYNC) |
| Connector | Fakra Z, metal shield |
| Camera size variants | 45 x 45 x 48.6 mm / 53.55 mm / 53.04 mm / 45.9 mm |
| Weight variants | 115 g / 142 g / 125 g / 107 g |
| Lens FoV variants (H/V, LDC OFF) | 30/19.5 deg, 63.5/41 deg, 120/73 deg, 175.3/105.3 deg |
| Lens mount | Glued, active alignment (non-exchangeable) |
| Power supply | Power over coax, 9 to 12 V |
| Power consumption | 4.6 W typ. at 30 fps, room temperature |
| Operating temperature | -40 to 85 C |
| Storage temperature | -40 to 105 C |
| Ingress protection | IP69K (with water-resistant Fakra cable) |
| Compliance | CE, RoHS, FCC, CAN ICES-3, UKCA, RCM, KC |

Reference:
https://tier4.github.io/edge-auto-docs/reference_manual/C2_technical_reference_manual.html
