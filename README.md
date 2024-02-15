# Weatherstation

This repository contains an embedded Linux system built for the
[Raspberry Pi 3 Model B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/)
using Buildroot ([https://buildroot.org/](https://buildroot.org/)).

This project runs a Python application that continiously reads from an
I2C-connected SHT31 temperature & humidity sensor, then writes the environmental
data to an SQLite database and functions as a webserver to visualize the results
on a dashboard.

For the individual projects providing sensor readings and dashboard
functionality, see [prdktntwcklr/python-sht31](https://github.com/prdktntwcklr/python-sht31)
and [prdktntwcklr/weatherman](https://github.com/prdktntwcklr/weatherman).

## Hardware

- Raspberry Pi 3 Model B+
- 32GB microSD card
- Sensirion SHT31 temperature & humidity sensor
- USB Micro-B cable
- RJ45 cable

## Building the project

First, make sure you have all mandatory packages for Buildroot readily installed
on your system. See the [Buildroot user manual section](https://buildroot.org/downloads/manual/manual.html#requirement-mandatory)
for details.

Since this repository contains several submodules, it needs to be cloned using
the `--recursive` flag:

```bash
git clone --recursive https://github.com/prdktntwcklr/weatherstation-linux.git
```

When building for the first time, the `BR2_EXTERNAL` variable needs to be set
to point to the out-of-tree directory:

```bash
cd weatherstation-linux/buildroot
make BR2_EXTERNAL=../buildroot-external weatherstation_defconfig
```

This loads the default configuration for the project. To build the project, run:

```bash
make -j16 2>&1 | tee ../build.log
```

Build messages will be stored in `build.log` under the top directory.
