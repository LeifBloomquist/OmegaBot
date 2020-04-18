import os
import time
import random

while (1):
  color = random.randint(0,0xffffff)
  os.system('expled ' + hex(color))
  print(hex(color))  
  time.sleep(1) 
