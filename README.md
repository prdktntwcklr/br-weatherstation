# Weatherstation

## Getting started

### Configure and build

When building for the first time, the BR2_EXTERNAL variable needs to be set to point to the correct directory:

```
cd buildroot
make BR2_EXTERNAL=../buildroot-external weatherstation_defconfig
make
```
