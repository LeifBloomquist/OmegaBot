from OmegaExpansion import pwmExp
import time
import timeit

#STEERING_ADJUST = 1.7
STEERING_ADJUST = 1.0


def Initialize():
  pwmExp.driverInit()
  Stop()
  return

def Stop():
   "This stops the robot"
   pwmExp.setupDriver(-1, 0, 0)   
   print "Stopped."
   return

def SetLeftRight( speed_left, speed_right):
   "This moves the robot forward with speeds for left and right"
   pwmExp.setupDriver(8, speed_left, 0)   
   pwmExp.setupDriver(7, speed_right * STEERING_ADJUST, 0)   
   return

def ForwardLeftRight( speed_left, speed_right, seconds ):
   "This moves the robot forward with speeds for left and right for a number of seconds"
   SetLeftRight(speed_left, speed_right)
   time.sleep(seconds)   
   Stop()
   return

def Forward( speed, seconds ):
   "This moves the robot forward"
   ForwardLeftRight(speed, speed, seconds)
   return


def Left( speed, seconds ):
   "This turns the robot left"
   ForwardLeftRight(speed, 0, seconds)
   return

def Right( speed, seconds ):
   "This turns the robot right"
   ForwardLeftRight(0, speed, seconds)
   return

Initialize()

Left(100, 2)
time.sleep(2)
Right(100, 2)
time.sleep(2)
Forward(100, 1)
Stop()

# Left(50, 2)
#ForwardLeftRight(100,10,2)


#init_time = timeit.timeit('Initialize()', setup="from __main__ import Initialize", number=10)
#set_time = timeit.timeit('SetLeftRight(50,50)', setup="from __main__ import SetLeftRight", number=10)
#stop_time = timeit.timeit('Stop()', setup="from __main__ import Stop", number=10)
#print "Initialize time: ", init_time
#print "Stop time: ", stop_time
#print "Set time: ", set_time
