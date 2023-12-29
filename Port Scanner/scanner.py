#!/bin/python3

#Building a port scanner
#A port scanner scan's a range of IP addresses or a single host for open ports, indicating which ports are currently accepting connections.
#The results of a port scan can help identify potential vulnerabilities or services running on a machine.

#create a scanner
#python3 scanner.py <ip>

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) ==2: #number of arguments we are giving argv[0] = scanner.py, arv[1] = ip
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 scanner.py <ip>")
	
#Not the best logic - but to start is fine
#Second step in the first if statement would be to make sure its a valid IP address, but we won't worry about that now

#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

#Exception handling
try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #1 second timeout, moves to the next
		result = s.connect_ex((target,port)) #tuple
		#port close = 1
		#port open = 1
		if result ==0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
except socket.error:
	print("Could not connect to the server.")
	sys.exit()
	

