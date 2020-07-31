import pyautogui
import time

x=1
while x<2:
    pyautogui.screenshot('/Users/INFO SYSTEM/Desktop/django/image'+str(x)+'.png')
    x+=1
    time.sleep(2)
