from OmegaExpansion import pwmExp
import time
import socket

PORT = 2000
STEERING_ADJUST = 1.7


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
   pwmExp.setupDriver(8, speed_right * STEERING_ADJUST, 0)
   return

Initialize()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(2.0)
s.bind(("", PORT))

print "Waiting on port: ", PORT


while True:

    try:
       data, addr = s.recvfrom(100)
       leftright = data.split(",")
       left = int(leftright[0])
       right = int(leftright[1])
       SetLeftRight(left, right)
       print "Received: ", data

    except socket.timeout:
       print "Receive timed out"
       Stop()

    except IndexError:
       print
       print "Data format error"
       Stop()
