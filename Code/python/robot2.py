import pins
import time
import onionGpio
from OmegaExpansion import pwmExp

LOW  = 0
HIGH = 1

# Instantiate

ain2 = onionGpio.OnionGpio(pins.AIN2)
ain1 = onionGpio.OnionGpio(pins.AIN1)
bin2 = onionGpio.OnionGpio(pins.BIN2)
bin1 = onionGpio.OnionGpio(pins.BIN1)

def robot_init():
  print("I/O Initialization")
  print("PWM Starting")
  pwmExp.driverInit()
  pwmExp.setupDriver(pins.ALL, 0, 0)
  pwmExp.setVerbosity(-1)

  print("Setting I/O")
  ain2.setOutputDirection(LOW)
  ain1.setOutputDirection(LOW)
  bin2.setOutputDirection(LOW)
  bin1.setOutputDirection(LOW)
  print("Ready!")

def safe():
  pwmExp.setupDriver(pins.ALL, 0, 0)
  ain1.setValue(LOW)
  ain2.setValue(LOW)
  bin1.setValue(LOW)
  bin2.setValue(LOW)

def standby(state):
  if state:
     pwmExp.setupDriver(pins.STBY, 100, 0)
     print("Standby Activated!")
  else:
     pwmExp.setupDriver(pins.STBY, 0, 0)
     print("Standby Disabled!")

def set_cw(io1, io2):
  io1.setValue(HIGH)
  io2.setValue(LOW)

def set_ccw(io1, io2):
  io1.setValue(LOW)
  io2.setValue(HIGH)

def set_speed(pwm, speed):
  pwmExp.setupDriver(pwm, speed, 0)

def stop():
  set_speed(pins.PWMA, 0)
  set_speed(pins.PWMB, 0)
  
def forward(speed, secs=0):
  set_cw(ain1, ain2)
  set_ccw(bin1, bin2)
  set_speed(pins.PWMA, speed)
  set_speed(pins.PWMB, speed)
  print "Forward at " + str(speed) + "%",
  
  if secs > 0:
    print "for " + str(secs) + " seconds"
    time.sleep(secs)
    stop()
  else:
    print ""

def reverse(speed, secs=0):
  set_ccw(ain1, ain2)
  set_cw(bin1, bin2)
  set_speed(pins.PWMA, speed)
  set_speed(pins.PWMB, speed)
  print "Reverse at " + str(speed) + "%",
  
  if secs > 0:
    print "for " + str(secs) + " seconds"
    time.sleep(secs)
    stop()
  else:
    print ""

def spin_left(speed, secs=0):
  set_ccw(ain1, ain2)
  set_ccw(bin1, bin2)
  set_speed(pins.PWMA, speed)
  set_speed(pins.PWMB, speed)
  print "Spinning left at " + str(speed) + "%",
  
  if secs > 0:
    print "for " + str(secs) + " seconds"
    time.sleep(secs)
    stop()
  else:
    print ""

def spin_right(speed, secs=0):
  set_cw(ain1, ain2)
  set_cw(bin1, bin2)
  set_speed(pins.PWMA, speed)
  set_speed(pins.PWMB, speed)
  print "Spinning Right at " + str(speed) + "%",
  
  if secs > 0:
    print "for " + str(secs) + " seconds"
    time.sleep(secs)
    stop()
  else:
    print ""

# For network control
                
def set_left_right(left, right):
  set_direction(right, ain1, ain2, pins.PWMA)
  set_direction(left, bin2, bin1, pins.PWMB)

def set_direction(speed, io1, io2, pin):
  if speed < 0:  
    set_ccw(io1, io2)
    speed = -speed
  else:
    set_cw(io1, io2)  
  
  set_speed(pin, speed)
