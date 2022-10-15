#! usr/bin/env python3


#importing libraris (ramdom):
from random import randint

#----------------------------

#function for emulation get data from sensor, from serial port (created by module random)
def get_data_from_serial_port():
	#command for return result of the random int, from 0 to 1024.
	return randint(0, 1024)
#----------------------------------------------------------------------------------------
