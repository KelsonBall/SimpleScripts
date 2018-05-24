# Sweep a range of IP addresses

help_text = """ 
pingsweep.py <https://github.com/Fallible/SimpleScripts>
Flags
 -h or --help
	description:
		prints this help text

 --address <address>
	description:
 		first 3 sections of ipv4 address
 	defaults to:
 		--address 10.11.1
	
--from <number>
	description:
		indicates start of sweep range
	defaults to:
		--from 1

--to <number>
	description:
		indicates end of sweep range
	defaults to:
		--to 255

--timeout <number>
	description:
		time to wait for first response, in seconds
	defaults to:
		None
"""
import os
from parse_args import Commands

commands = Commands([]) # get command line args

if commands.has_flag("h") or commands.has_flag("help"):
	print(help_text)
else:
	# read from args or use default
	ping_command = "ping -c 1"
	if commands.has_flag("timeout"):
		ping_command += " -W " + str(commands.int_of("timeout"))
	ping_command += " " + (commands.string_of("address") or "10.11.1") + "."

	start = commands.int_of("from") or 1
	end = (commands.int_of("to") or 255) + 1
	

	# sweep address space from 'start' to 'end'
	for ip in range (start, end):
		os.system(ping_command + str(ip))

