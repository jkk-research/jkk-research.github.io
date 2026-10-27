# Stereolabs ZED 2i vs ZED 2 Datasheet (Short)

<p>
  <img src="https://cdn.sanity.io/images/s18ewfw4/staging/a3348b200a33da0fe38860442c1b7ac11af24f84-4000x4000.png?rect=334,751,3332,2499&w=520&q=80&auto=format" alt="ZED 2i" width="48%" />
  <img src="https://cdn.sanity.io/images/s18ewfw4/staging/cee1ff1fb481391c5fa835533faa25102e341bc8-4000x4000.png?rect=0,0,3668,3475&w=520&q=80&auto=format" alt="ZED 2 family" width="48%" />
</p>

## Technical specifications

| Parameter | ZED 2i | ZED 2 |
|---|---|---|
| Stereo baseline | 120 mm | 120 mm |
| Video modes | 2K@15, 1080p@30, 720p@60, 672x376 up to 100 FPS | 2K@15, 1080p@30, 720p@60, 672x376 up to 100 FPS |
| Shutter | Synchronized rolling shutter | Synchronized rolling shutter |
| Interface | USB Type-C with dual locking screws | USB Type-C |
| Depth range (typical) | 0.3 to 20 m (2.1 mm) or 1.5 to 35 m (4 mm) | Shorter practical range than 2i (model dependent) |
| Lens options | 2.1 mm or 4 mm, optional CPL | More limited optics options |
| Onboard sensors | IMU + barometer + magnetometer + temperature | IMU-centric configuration |
| Ruggedization | IP66 | Lower environmental protection than ZED 2i |

## ROS 2 Driver

- [zed-ros2-wrapper](https://github.com/stereolabs/zed-ros2-wrapper) - Official ROS 2 wrapper

## References

- https://www.stereolabs.com/en-hu/products/zed-2
- https://www.stereolabs.com/en-hu/products/zed-2i
- https://www.stereolabs.com/en-hu/products/zed-x
