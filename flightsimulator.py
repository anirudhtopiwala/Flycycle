# -*- coding: utf-8 -*-
import win32api, win32con
import serial 


# Initial Cursor Position
cx = 0
xMax = 1900
cy = 0
yMax = 1000

Sensitivity = .5        # Higher numbers make the mouse movement less sensitive to Tilt

ser = serial.Serial('COM4', timeout=2)
          
ser.flushInput()                # Discard Buffer Contents

enCursor =  0     # Start with the Cursor Disbled
l1state = 0
r1state = 0
l1stateD1 = 0
r1stateD1 = 0                                    


#def l1Pressed():
#    return l1stateD1 - l1state  # 0,1,-1 : Same, Just Pressed, Just Released
#
#def r1Pressed():
#    return r1stateD1 - r1state  # 0,1,-1 : Same, Just Pressed, Just Released
(cx,cy) = win32api.GetCursorPos()

while 1:
    # Read a line and separate the newline characters from the rest
    rx = ser.readline().decode().split('\r\n')
#    print(rx)   # Debug 
    # Now separate the data from the commas
    data = rx[0].split(',')
    xTilt = int(data[1])
    yTilt = int(data[0])
    l1stateD1 = l1state
    r1stateD1 =  r1state
    l1state = int(data[2])
    r1state = int(data[3])
  
    x = 959 + xTilt/Sensitivity        #  x-Cursor = centre value (when button was pressed) + Tilt value
    x = max(min(xMax, x), 0)       # Limit to the Screen co-or dinates 
    y = 532 - yTilt/Sensitivity       # y-Cursor = cen tre value (when button was pressed) + Tilt value
    y = max(min(yMax, y), 0)         # Limit to the Screen co-ordinates 

#    l1 = l1Pressed()            # Check the Button
#    r1 = r1Pressed()            # Check the Button
#    print(l1)
    l1 = l1state
    r1 = r1state
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
#        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(x),int(y),0,0)
#        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(x),int(y),0,0)
        print(cx)
        print(cy)
        win32api.SetCursorPos((int(x),int(y)))
        print("Simulation Running")

# We're Done. Close the Serial Port
print("SImulation FInshed")
ser.close()