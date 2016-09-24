#!/usr/bin/python
import ledpy
import sys
import time
if __name__ == '__main__':
    led = [17, 27, 22, 10, 9]
    led_sec = [11, 5, 6, 13, 19]
#    led = [5]
#    led_sec = [4]
    ledpy.Init_Led_Port(True,led, led_sec)
    time.sleep(1)
    cmd = int(sys.argv[1])
    if cmd == 0:
        ledpy.SetDualForced_BootUp()
    elif cmd == 1:
        ledpy.SetDualForced_Shutdown()
    elif cmd == 2:
        ledpy.SetDualLedOff()
    elif cmd == 3:
	    ledpy.SetDualLedOn()
    elif cmd == 4:
	    ledpy.SetDualLedSmoothOn()
    elif cmd == 5:
	    ledpy.SetDualLedSmoothOff()
    elif cmd == 6:
	    ledpy.SetDualLedRightShiftOff()
    elif cmd == 7:
	    ledpy.SetDualLedRightShiftOn()
    elif cmd == 8:
	    ledpy.SetDualLedLeftShiftOff()
    elif cmd == 9:
	    ledpy.SetDualLedLeftShiftOn()
    elif cmd == 10:
	    ledpy.SetLedRightTurn()
    elif cmd == 11:
	    ledpy.SetLedLeftTurn()
    elif cmd == 12:
        for k in range(10):
             ledpy.SetDualLedSmoothOff()
             time.sleep(0.2)
             ledpy.SetDualLedSmoothOn()
             time.sleep(0.2)
