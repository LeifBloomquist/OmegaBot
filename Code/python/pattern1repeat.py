from robot2 import *

robot_init()
standby(True)

for _ in range(10):
  forward(50,2)
  reverse(50,2)
  spin_left(60,2)
  spin_right(60,2)

safe()
