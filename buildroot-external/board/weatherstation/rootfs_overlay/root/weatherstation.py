#!/usr/bin/env python

import smbus
import sqlite3
import sys
import time

from sht31 import sht31

address = 0x44  # default address
bus = smbus.SMBus(1)

try:
    sht31 = sht31.SHT31(address=address, bus=bus)
except Exception as e:
    print("Initializing SHT31 failed:", e)
    sys.exit(1)

# TODO: database file should be created from within Python if it does not exist (see notes.text for command)
#       and not manually using sqlite3 utility
# TODO: date format uses epoch time (starts from 1970-01-01 00:00:00) at the moment, change to actual date and time
# TODO: temperature and humidity use more than two decimal places, change to two

def log_values(temperature, humidity):
	conn=sqlite3.connect('/var/www/weatherstation/weather.db')  # must be absolute path

	curs=conn.cursor()
	curs.execute("""INSERT INTO database values(datetime(CURRENT_TIMESTAMP, 'localtime'),
         (?), (?))""", (temperature, humidity))
	conn.commit()

	conn.close()

while True:
    temperature, humidity = sht31.get_temp_and_humidity()

    if temperature is not None and humidity is not None:
        print("Temperature: {:.2f}°C".format(temperature))
        print("Relative humidity: {:.2f}%".format(humidity))
        log_values(temperature, humidity)
    else:
        print("Failed to read SHT31! Check if sensor is connected.")
        log_values("1", -99.99, -99.99)  # dummy value if sensor read fails

    time.sleep(1)
