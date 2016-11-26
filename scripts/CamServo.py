#!/usr/bin/env python

import time
import pigpio

#set servo GPIO pins
panGPIO = 39 #(side to side movement)
tiltGPIO = 40 #()

#set servos to default location on start up of code
panpw = 1500
tiltpw = 1500


#use the pigpio service
pi = pigpio.pi() # Connect to local Pi.

#set the servos to default locations
pi.set_servo_pulsewidth(panGPIO, panpw)
pi.set_servo_pulsewidth(tiltGPIO, tiltpw)


def CamServo(pan, tilt)

	try:
	#change the pan of the camera mount
		if (pan.lower() == 'l'):
			panpw = 800
		if (pan.lower() == 'm'):
			panpw = 1500
		if (pan.lower() == 'r')
			panpw = 2200			
		if (pan.lower() == 'reset'):
			panpw = 1500
	#change the tilt of the camera mount				
		if (tilt.lower() == 'd'):
			tiltpw = 800
		if (tilt.lower() == 'm'):
			tiltpw = 1500
		if (tilt.lower() == 'u')
			tiltpw = 2200			
		if (tilt.lower() == 'reset'):
			tiltpw = 1500
					
		pi.set_servo_pulsewidth(panGPIO, panpw)
		pi.set_servo_pulsewidth(tiltGPIO, tiltpw)

	except:
		print ("Pan Tilt ERROR")
		pi.set_servo_pulsewidth(panGPIO, 1500)
		pi.set_servo_pulsewidth(tiltGPIO, 1500)		

			
