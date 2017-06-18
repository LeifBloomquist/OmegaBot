from OmegaExpansion import pwmExp
import time
import socket

port = 2000

def Initialize():
  pwmExp.driverInit()
  Stop()
  return

def Stop():
   "This stops the robot"
   pwmExp.setupDriver(-1, 0, 0)
   return

def SetLeftRight( speed_left, speed_right):
   "This moves the robot forward with speeds for left and right"
   pwmExp.setupDriver(7, speed_left, 0)
   pwmExp.setupDriver(8, speed_right, 0)
   return

Initialize()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5.0)
s.bind(("", port))

print "Waiting on port: ", port

while True:

    try:
       data, addr = s.recvfrom(100)
       print "Received: ", data
       leftright = data.split(",")
       left = int(leftright[0])
       right = int(leftright[1])
       print "   Left: ", left
       print "   Right: ", right
       SetLeftRight(left, right)

    except socket.timeout:
       print "Receive timed out"
       Stop()

    except IndexError:
       print
       print "Data format error"
       Stop()