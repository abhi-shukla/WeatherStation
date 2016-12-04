import time
import grovepi
import random
import decimal
from grove_rgb_lcd import *

#Grove Temprature Sensor at A0
sensor = 0

while True:
	try:
		temp = grovepi.temp(sensor, '1.1')
		cel = round(temp, 0)
		print(str(cel))
		setText('It is ' + str(cel) + ' Celcius')
		if cel <10.0:
			setRGB(0,255,255)
		elif cel>=10.0 and cel<20.0:
			setRGB(102,204,0)
		elif cel >= 20.0 and cel <30.0:
			setRGB(255,128,0)
		elif cel >=30.0:
			setRGB(255,0,0)
		time.sleep(300)

	except KeyboardInterrupt:
		break
	except IOError:
		print ("Error")

