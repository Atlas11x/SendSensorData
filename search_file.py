#!/usr/bin/env python3

#import libraris
import os

while True:
	check_file = os.path.exists("./probBash.txt")

	if check_file:
		print("YES: file exists")
		break
	else:
		print("NO: file not exists")

	