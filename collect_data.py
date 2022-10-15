#!/usr/bin/env python3

#import libraris
import random
import os
import emu

#init varriables
data = open("unit.txt", "w")
file_len = 20

#main code (loop)
while True:
	for i in range(file_len):
		data.write(str(emu.get_data_from_serial_port())+"\n")
	break
