import pins
import time
import onionGpio
from OmegaExpansion import pwmExp

LOW  = 0
HIGH = 1

# 0. Init

print("I/O Initialization")

# Instantiate

ain2 = onionGpio.OnionGpio(pins.AIN2)
ain1 = onionGpio.OnionGpio(pins.AIN1)
bin2 = onionGpio.OnionGpio(pins.BIN2)
bin1 = onionGpio.OnionGpio(pins.BIN1)

# All Outputs, low default

print("PWM Starting")

pwmExp.driverInit()
pwmExp.setupDriver(pins.ALL, 0, 0)

print("Setting I/O")

ain2.setOutputDirection(LOW)
ain1.setOutputDirection(LOW)
bin2.setOutputDirection(LOW)
bin1.setOutputDirection(LOW)

print("Ready")

# 1. Set Standby to HIGH

pwmExp.setupDriver(pins.STBY, 100, 0)

################################# A

# 2. Set direction CW

ain1.setValue(HIGH)
ain2.setValue(LOW)

# 3. Enable PWM

pwmExp.setupDriver(pins.PWMA, 25, 0)

# 4. Pause for a bit

time.sleep(5)

# 2. Set direction CCW

ain1.setValue(LOW)
ain2.setValue(HIGH)

time.sleep(5)

# 5. Stop

pwmExp.setupDriver(pins.ALL, 0, 0)
