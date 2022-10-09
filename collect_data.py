#!/usr/bin/env python3

#import libraris
import random
import os

#init varriables
data = open("unit.txt", "w")
file_len = 20

#create emulator
def sp():
	return random.randint(0, 1024)

#main code (loop)
while True:
	for i in range(file_len):
		data.write("n/"+str(sp))
	break
