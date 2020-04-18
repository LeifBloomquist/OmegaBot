import serial
import time

ser = serial.Serial('/dev/ttyS1', 2400)  # open serial port
print(ser.name)         # check which port was really used

b=1

while (True):
    ser.write('Hello ' + str(b) + '\r\n')     # write a string
    b=b+1
    time.sleep(0.2)

ser.close()             # close port
