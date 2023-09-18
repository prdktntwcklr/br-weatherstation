################################################################################
#
# python-sht31
#
################################################################################

PYTHON_SHT31_VERSION = 0.0.1
PYTHON_SHT31_SOURCE = python-sht31-$(PYTHON_SHT31_VERSION).tar.gz
PYTHON_SHT31_SITE = https://github.com/prdktntwcklr/python-sht31/releases/download/v$(PYTHON_SHT31_VERSION)
PYTHON_SHT31_SETUP_TYPE = setuptools
PYTHON_SHT31_LICENSE = MIT
PYTHON_SHT31_LICENSE_FILES = LICENSE

$(eval $(python-package))
