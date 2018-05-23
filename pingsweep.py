import os

for ip in range (1, 255):
	os.system("ping -c 1 10.11.1." + str(ip))

