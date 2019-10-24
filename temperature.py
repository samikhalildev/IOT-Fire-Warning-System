import sys
import time

from envirophat import weather, leds, light, motion

unit = 'hPa'

try:
    while True:
	rgb = light.rgb()
	motion_magnetometer = motion.magnetometer()
        temperature = weather.temperature()

        temp = "Temp:{0: .2f}c".format(temperature)
	write(temp)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
