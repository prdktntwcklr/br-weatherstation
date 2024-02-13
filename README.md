# Weatherstation

## Getting started

### Configure and build

When building for the first time, the `BR2_EXTERNAL` variable needs to be set
to point to the out-of-tree directory:

```
cd buildroot
make BR2_EXTERNAL=../buildroot-external weatherstation_defconfig
make -j16 2>&1 | tee ../build.log
```
