import pyautogui
import time
import sys
from datetime import datetime
from idle_time import IdleMonitor

pyautogui.FAILSAFE = False
numMin = None
monitor = IdleMonitor.get_monitor()

if ((len(sys.argv) < 2) or sys.argv[1].isalpha() or int(sys.argv[1]) < 1):
   numMin = 3
else:
   numMin = int(sys.argv[1])

while(True):
  y = monitor.get_idle_time()
  x=0
  while (x<numMin):
      time.sleep(60)
      x += 1
  if ((numMin*60)<y):
      for i in range(1, 10):
          pyautogui.moveTo(1, i * 4)
      pyautogui.moveTo(1, 1)
      for i in range(0, 3):
          pyautogui.press("ctrl")
      print("Movement made at {}".format(datetime.now().time()))
      print("Idle time {} sec.".format(y))
