import time
import socket
from robot2 import *           

# Constants

PORT = 2000
STEERING_ADJUST = 1.0

robot_init()
standby(True)

# Listen for network packet

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
       set_left_right(left, right)
       print "Received: ", data

    except socket.timeout:
       print "Receive timed out"
       stop()

    except IndexError:
       print
       print "Data format error"
       stop()
