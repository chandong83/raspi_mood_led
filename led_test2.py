#!/usr/bin/python
import ledpy
import sys
import time
if __name__ == '__main__':
    led_sec = [17, 27, 22, 10, 9]
    led = [11, 5, 6, 13, 19]
#    led = [5]
#    led_sec = [4]
    ledpy.Init_Led_Port(True,led, led_sec)
    t = 0.5
    time.sleep(1)
    cmd = int(sys.argv[1])
    ledpy.SetDualForced_BootUp()
    time.sleep(t)
    ledpy.SetDualForced_Shutdown()
    time.sleep(t)
    ledpy.SetDualLedOn()
    time.sleep(t)
    ledpy.SetDualLedOff()
    time.sleep(t)
    ledpy.SetDualLedSmoothOn()
    time.sleep(t)
    ledpy.SetDualLedSmoothOff()
    time.sleep(t)
    ledpy.SetDualLedRightShiftOn()
    time.sleep(t)
    ledpy.SetDualLedRightShiftOff()
    time.sleep(t)
    ledpy.SetDualLedLeftShiftOn()
    time.sleep(t)
    ledpy.SetDualLedLeftShiftOff()
    ledpy.SetLedRightTurn()
    #ledpy.SetLedLeftTurn()    
    for k in range(10):
       ledpy.SetDualLedSmoothOff()
       time.sleep(0.2)
       ledpy.SetDualLedSmoothOn()
       time.sleep(0.2)
