# -*- coding: utf-8 -*-
import win32api, win32con
import serial 
import time
try:
    ser = serial.Serial('COM4', timeout=2,baudrate = 9600)
except:
    print("Remember to close the serial port nxt time")
          
ser.flushInput()    # Discard Buffer Contents

l1 = 0
l2 = 0 
r1 = 0
r2 = 0

while 1:
    # Read a line and separate the newline characters from the rest
    rx = ser.readline().decode().split('\r\n')
#    print(rx)   # Debug 
    # Now separate the data from the commas
    data = rx[0].split(',')
    pitch = int(data[0])
    roll = int(data[1])
    l2 = int(data[2])
    l1 = int(data[3])
    r1 = int(data[4])
    r2 = int(data[5])
#    time.sleep(1)
    if (r2==0):
        win32api.keybd_event(0x53, 0,0,0)    # PRESS S for Breaking
#        time.sleep(0.5)
        win32api.keybd_event(0x53,0 ,win32con.KEYEVENTF_KEYUP ,0)
        print("Breaking") 
    elif (l2==0):
          # Braking
        win32api.keybd_event(0x20, 0,0,0)    # PRESS Space for nitros
        win32api.keybd_event(0x20,0 ,win32con.KEYEVENTF_KEYUP ,0)
        print("Nitros Engaged")
    elif (l1==0 and r1==0):
        print("End of Game Control")
        break
    elif (l1==0):
          # Re-Spawning
        win32api.keybd_event(0x51, 0,0,0)    # PRESS Q for Respawn
        win32api.keybd_event(0x51,0 ,win32con.KEYEVENTF_KEYUP ,0)
        print("Respawn")
    elif (r1==0):
          #Change Cmaera Angle
        win32api.keybd_event(0x43, 0,0,0)    # PRESS Q for Respawn
        win32api.keybd_event(0x43,0 ,win32con.KEYEVENTF_KEYUP ,0)
        print("Changing Cmaera Angle")
        
    
    if(roll> 40):
        win32api.keybd_event(0x44, 0,0,0)    # PRESS D for Going Right
        win32api.keybd_event(0x44,0 ,win32con.KEYEVENTF_KEYUP ,0)
        print("Going Right")
    elif (roll < -40):
        win32api.keybd_event(0x41, 0,0,0)    # PRESS A for Going Left
        win32api.keybd_event(0x41,0 ,win32con.KEYEVENTF_KEYUP ,0)
        print("Going Left")
#    elif (pitch > 180):
#        win32api.keybd_event(0x53, 0,0,0)    # PRESS S for Breaking
#        win32api.keybd_event(0x53,0 ,win32con.KEYEVENTF_KEYUP ,0)
#        print("Breaking")
#        
    

# We're Done. Close the Serial Port
print("SImulation FInshed")
ser.close()