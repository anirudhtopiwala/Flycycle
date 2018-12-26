# -*- coding: utf-8 -*-
import win32api, win32con
import serial 

# Initial Cursor Position
cx = 0
xMax = 1900
cy = 0
 
Sensitivity = .5        # Higher numbers make the mouse movement less sensitive to Tilt

try:
    ser = serial.Serial('COM4', timeout=2,baudrate = 9600)
except:
    print("Remember to close the serial port nxt time")
          
ser.flushInput()    # Discard Buffer Contents

l1 = 0
l2 = 0 
r1 = 0
r2 = 0
enCursor =  0     # Start with the Cursor Disbled
 
while 1:
    # Read a line and separate the newline characters from the rest 
    rx = ser.readline().decode().split('\r\n')
#    print(rx)   # Debug 
    # Now separate the data from the commas
    data = rx[0].split(',')
    yTilt = int(data[0])
    xTilt = int(data[1])
    l2 = int(data[2])
    l1 = int(data[3])
    r1 = int(data[4])           
    r2 = int(data[5])
  
    x = 959 + xTilt/Sensitivity        #  x-Cursor = centre value (when button was pressed) + Tilt value
    x = max(min(xMax, x), 0)       # Limit to the Screen co-or dinates 
    y = 500 + yTilt/Sensitivity       # y-Cursor = cen tre value (when button was pressed) + Tilt value
    y = max(min(yMax, y), 0) # Limit to the Screen co-ordinates 

#    print("l1", l1) 
#    print("r1", r1)
# Disable the cursor if it's Enabled now and the switch is pressed
    if (l1 ==0 and r1==0):
        enCursor = 0
        win32api.keybd_event(0x20, 0,0,0)    # PRESS the SPACE Key to Pause Flight Simulator
        win32api.keybd_event(0x20,0 ,win32con.KEYEVENTF_KEYUP ,0)
        print("Ending Simulation")  
        break   
    elif (r1==0):
        enCursor = 0
#        win32api.keybd_event(0x20, 0,0,0)    # PRESS the SPACE Key to Pause Flight Simulator
#        win32api.keybd_event(0x20,0 ,win32con.KEYEVENTF_KEYUP ,0) 
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(x),int(y),0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(x),int(y),0,0)               
        print("Pausing Simulation")
# Enable the cursor if it's Disabled now and the switch is pressed
    elif (l1==0):
        enCursor = 1
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(x),int(y),0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(x),int(y),0,0)
    elif (l2==0 and r2==0):
        win32api.keybd_event(0x21, 0,0,0)    # PRESS S for Breaking
        win32api.keybd_event(0x21,0 ,win32con.KEYEVENTF_KEYUP ,0)
        print("Accelerating") 
#        l1=0
#    elif (enCursor and l1 != 1):
#        enCursor = 0
#        win32api.keybd_event(0x20, 0,0,0)    # PRESS the SPACE Key to Pause Flight Simulator
#        win32api.keybd_event(0x20,0 ,win32con.KEYEVENTF_KEYUP ,0)
#    elif (enCursor and l1==1):
#        enCursor =0
#  
    if enCursor:  
        (cx,cy) = win32api.GetCursorPos()
        win32api.SetCursorPos((int(x),int(y)))
        print("Simulation Running")

# We're Done. Close the Serial Port
print("SImulation FInshed")
ser.close()