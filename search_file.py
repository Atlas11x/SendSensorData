#!/usr/bin/env python3

#import libraris
import os

while True:
	try:
		check_file = os.path.exists("./probBash.txt")
	
		if check_file:
			print("YES: file exists")
			break
		else:
			print("NO: file not exists")
	except:
		print("Error, retrying...")
