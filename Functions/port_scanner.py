import socket
import sys

# Defining a target
if len(sys.argv) == 2:     
  # translate hostname to IPv4
  target = socket.gethostbyname(sys.argv[1])
else:
  print("Invalid amount of Argument")
    
for port in range(1,65535):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.setdefaulttimeout(1)
  # returns an error indicator
  result = s.connect_ex((target,port))
  if result ==0:
    print("Port {} is open".format(port))
  s.close()