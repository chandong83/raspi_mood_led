#!/usr/bin/python
import ledpy
import sys
if __name__ == '__main__':
    led = [2, 3, 4, 17, 27]
    ledpy.Init_Led_Port(led)

    cmd = int(sys.argv[1])
    if cmd == 0:
        ledpy.SetForced_BootUp()
    elif cmd == 1:
        ledpy.SetForced_Shutdown()
    elif cmd == 2:
	ledpy.SetLedOff()
    elif cmd == 3:
	ledpy.SetLedOn()
    elif cmd == 4:
	ledpy.SetLedSmoothOn()
    elif cmd == 5:
	ledpy.SetLedSmoothOff()
    elif cmd == 6:
	ledpy.SetLedRightShiftOff()
    elif cmd == 7:
	ledpy.SetLedRightShiftOn()
    elif cmd == 8:
	ledpy.SetLedLeftShiftOff()
    elif cmd == 9:
	ledpy.SetLedLeftShiftOn()
    elif cmd == 10:
	ledpy.SetLedRightTurn()
    elif cmd == 11:
	ledpy.SetLedLeftTurn()
