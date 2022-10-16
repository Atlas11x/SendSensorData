#!/usr/bin/env python3


#importing libraris
import serial
import time
import os

#Get data from serial port
port = serial.Serial("/dev/ttyUSB0", 9600)
time.sleep(2)
list_data = []

#Process getting data
while True:
	line = port.readline()
	#print(line)
	#b'123\r\n'
	
#first way:
	string = line.decode()
	#print(string)
	#print(len(string))
	
	#list_ = string.split('\r')
	#print(list_)
	#print(list_[0])
#Second way:
	stripped_string = string.strip()
	#with \r, \n
	#print(string)
	#wihout \r, \n
	print(stripped_string)
	list_data.append(stripped_string)
	if len(list_data) == 22:
		os.system("/home/oztm/Atlas_/SendSensorData_ver2/SendSensorData/hello_in_file.sh &")
		break
	
	#for math operations
	num_int = int(stripped_string)
	#if num_int == 999:
		#break	
print ("++++")

try:
	f = open("./unit.txt", 'w')
	for i in range(len(list_data)):
		f.write(list_data[i])
		f.write("\n")
	f.close()
except OSError as e:
	print (e.args)
	print("Error")
	f = open("./unit.txt", 'w')
	f.close()
	#exit()
port.close()