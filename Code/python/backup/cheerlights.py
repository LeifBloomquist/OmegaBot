import urllib
import os
import time

link = "http://api.thingspeak.com/channels/1417/field/2/last.txt"

while (1):
  f = urllib.urlopen(link)
  color = f.read() 
  color = color.replace("#", "0x")
  print "Setting LED to " + color
  os.system("expled " + color)
  time.sleep(5)
