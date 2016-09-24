#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import threading
import random

#LED Port Setting
led = []
led_second = []
bDualLED = False
#led = [17, 27, 22, 23, 24, 25, 5, 6, 13, 19]


led_step = 0.0005
led_frequency = 0.018
led_loop_step = 35 # led_frequency / led_step - 1


#LED Mode
led_mode_on_off = 0
led_mode_off = 1
led_mode_on = 2

led_motion_speed = 0.15

def Init_Led_Port(dual, led_port, led_second_port):
    global led
    global led_second
    led  = led_port
    GPIO.setmode(GPIO.BCM)
    for k in led:
        GPIO.setup(k, GPIO.OUT)
        GPIO.output(k, False)



    # Dual Mode
    if dual == True:
        led_second = led_second_port
        for k in led_second:
            GPIO.setup(k, GPIO.OUT)
            GPIO.output(k, False)





class led_thread(threading.Thread):
    def __init__(self, led_port, mode):
        super(led_thread, self).__init__()

        self.led_port = led_port
        self.mode = mode

        self.__isRunning = True

        self.led_off = led_frequency
        self.led_on  = 0.000

    def run(self):
        if self.mode == led_mode_on_off:
            for i in range(led_loop_step):
                #for j in range(1):
                GPIO.output(self.led_port, False)
                time.sleep(self.led_off)
                GPIO.output(self.led_port, True)
                time.sleep(self.led_on)

                self.led_off = self.led_off - led_step
                self.led_on = self.led_on + led_step

            for i in range(led_loop_step):
                #for j in range(1):
                GPIO.output(self.led_port, True)
                time.sleep(self.led_on)
                GPIO.output(self.led_port, False)
                time.sleep(self.led_off)

                self.led_off = self.led_off + led_step
                self.led_on = self.led_on - led_step



        elif self.mode == led_mode_off:
            self.led_off = 0.000
            self.led_on  = led_frequency
            for i in range(led_loop_step):
                GPIO.output(self.led_port, True)
                time.sleep(self.led_on)
                GPIO.output(self.led_port, False)
                time.sleep(self.led_off)

                self.led_off = self.led_off + led_step
                self.led_on = self.led_on - led_step



        elif self.mode == led_mode_on:
            for i in range(led_loop_step):
                GPIO.output(self.led_port, False)
                time.sleep(self.led_off)
                GPIO.output(self.led_port, True)
                time.sleep(self.led_on)

                self.led_off = self.led_off - led_step
                self.led_on = self.led_on + led_step



    def finish(self):
        self.__isRunning = False


#
# Smoothly Turn on left to right LED
# and then Smoothly Turn off right to left it
#
def SetLedLeftTurn():
    Threads = []
    Threads_reverse = []

    SetLedOff()

    for i in led:
        th = led_thread(i, led_mode_on_off)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(led_motion_speed)

    for th in Threads:
        th.join()


    led_reverse = led[:]
    led_reverse.reverse()

    for i in led_reverse:
        th = led_thread(i, led_mode_on_off)
        Threads_reverse.append(th)

    for th in Threads_reverse:
        th.start()
        time.sleep(led_motion_speed)

    for th in Threads_reverse:
        th.finish()
        th.join()


#
# Smoothly Turn on right to left LED
# and then Smoothly Turn off left to right it
#
def SetLedRightTurn():
    Threads = []
    Threads_reverse = []

    led_reverse = led[:]
    led_reverse.reverse()

    for i in led_reverse:
        th = led_thread(i, led_mode_on_off)
        Threads_reverse.append(th)

    for th in Threads_reverse:
        th.start()
        time.sleep(led_motion_speed)

    for th in Threads_reverse:
        th.finish()
        th.join()

    led_reverse.reverse()

    for i in led_reverse:
        th = led_thread(i, led_mode_on_off)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(led_motion_speed)

    for th in Threads:
        th.join()





def SetLedLeftShiftOn( onoff ):
    Threads = []

    for i in led:
        th = led_thread(i, onoff)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(led_motion_speed)

    for th in Threads:
        th.join()

#
# Smoothly Turn on left to right All LED
#
def SetLedLeftShiftOn():
    SetLedLeftShiftOn( led_mode_on )


#
# Smoothly Turn off left to right All LED
#
def SetLedLeftShiftOff():
    SetLedLeftShiftOn( led_mode_off )



def SetDualLedLeftShift( onoff ):
    Threads = []
    Threads_second = []

    index = 0
    for i in led:
        th = led_thread(i, onoff)
        th_second = led_thread(led_second[index], onoff)
        Threads_second.append(th_second)
        Threads.append(th)
        index = index + 1

    index = 0
    for th in Threads:
        Threads_second[index].start()
        th.start()
        time.sleep(led_motion_speed)
        index = index + 1

    index = 0
    for th in Threads:
        th.finish()
        Threads_second[index].finish()
        th.join()
        Threads_second[index].join()
        index = index + 1

#
# Smoothly Turn on left to right All Dual LED
#
def SetDualLedLeftShiftOn():
    SetDualLedLeftShift( led_mode_on )


#
# Smoothly Turn off left to right All Dual LED
#
def SetDualLedLeftShiftOff():
    SetDualLedLeftShift( led_mode_off )


def SetLedRightShift( onoff ):
    Threads = []

    led_reverse = led[:]
    led_reverse.reverse()

    for i in led_reverse:
        th = led_thread(i, onoff)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(led_motion_speed)

    for th in Threads:
        th.join()
#
# Smoothly Turn on right to left All LED
#
def SetLedRightShiftOn():
    SetLedRightShift(led_mode_on)


#
# Smoothly Turn off right to left All LED
#
def SetLedRightShiftOff():
    SetLedRightShift(led_mode_off)


def SetDualLedRightShift( onoff ):
    Threads = []
    Threads_second = []

    led_reverse = led[:]
    led_reverse.reverse()

    led_second_reverse = led_second[:]
    led_second_reverse.reverse()


    index = 0
    for i in led_reverse:
        th = led_thread(i, onoff)
        th_second = led_thread(led_second[index], onoff)
        Threads_second.append(th_second)
        Threads.append(th)
        index = index + 1


    index = 0
    for th in Threads:
        Threads_second[index].start()
        th.start()
        time.sleep(led_motion_speed)
        index = index + 1

    index = 0
    for th in Threads:
        th.finish()
        Threads_second[index].finish()
        th.join()
        Threads_second[index].join()
        index = index + 1

#
# Smoothly Turn on right to left All Dual LED
#
def SetDualLedRightShiftOn():
    SetDualLedRightShift(led_mode_on)


#
# Smoothly Turn off right to left All Dual LED
#
def SetDualLedRightShiftOff():
    SetDualLedRightShift(led_mode_off)


#
# Smoothly Turn On  All LED
#
def SetLedSmooth( onoff ):
    Threads = []

    for i in led:
        th = led_thread(i, onoff)
        Threads.append(th)

    for th in Threads:
        th.start()

    for th in Threads:
        th.finish()
        th.join()
#
# Smoothly Turn Off  All LED
#
def SetLedSmoothOff():
    SetLedSmooth(led_mode_off)


#
# Smoothly Turn On  All LED
#
def SetLedSmoothOn():
    SetLedSmooth(led_mode_on)




def SetDualLedSmooth( onoff ):
    Threads = []
    Threads_second = []
    index = 0
    for i in led:
        th = led_thread(i, onoff)
        th_second = led_thread(led_second[index], onoff)
        Threads_second.append(th_second)
        Threads.append(th)
        index = index + 1

    index = 0
    for th in Threads:
        tmp = Threads_second[index]
        tmp.start()
        th.start()
        index = index + 1

    index = 0
    for th in Threads:
        th.finish()
        Threads_second[index].finish()

        th.join()
        Threads_second[index].join()

        index = index + 1


#
# Smoothly Turn Off  All Dual LED
#
def SetDualLedSmoothOff():
    SetDualLedSmooth(led_mode_off)

#
# Smoothly Turn On  All Dual LED
#
def SetDualLedSmoothOn():
    SetDualLedSmooth(led_mode_on)




def SetLed( onoff ):
    for k in led:
        GPIO.output(k, onoff)

#
# Turn On All LED
#
def SetLedOn():
    SetLed(True)

#
# Turn Off All LED
#
def SetLedOff():
    SetLed(False)


def SetDualLed( onoff ):
    index = 0
    for k in led:
        GPIO.output(k, onoff)
        GPIO.output(led_second[index], onoff)
        index = index + 1


#
# Turn On All Dual LED
#
def SetDualLedOn():
    SetDualLed(True)


#
# Turn Off All Dual LED
#
def SetDualLedOff():
    SetDualLed(False)


#
# System Shutdown LED Effect
#
def SetForced_Shutdown():
    for n in xrange(3):
        SetLedOn()
        time.sleep(0.05)
        SetLedOff()
        time.sleep(0.05)

    time.sleep(0.3)
    SetLedOn()

    time.sleep(0.5)
    SetLedSmoothOff()


#
# System BootUp LED Effect
#
def SetForced_BootUp():
    for n in xrange(3):
        SetLedOn()
        time.sleep(0.05)
        SetLedOff()
        time.sleep(0.05)

    time.sleep(0.3)
    SetLedOff()

    time.sleep(0.5)
    SetLedSmoothOn()



#
# System Shutdown Dual LED Effect
#
def SetDualForced_Shutdown():
    for n in xrange(3):
        SetDualLedOn()
        time.sleep(0.05)
        SetDualLedOff()
        time.sleep(0.05)

    time.sleep(0.3)
    SetDualLedOn()

    time.sleep(0.5)
    SetDualLedSmoothOff()


#
# System BootUp Dual LED Effect
#
def SetDualForced_BootUp():
    for n in xrange(3):
        SetDualLedOn()
        time.sleep(0.05)
        SetDualLedOff()
        time.sleep(0.05)

    time.sleep(0.3)
    SetDualLedOff()

    time.sleep(0.5)
    SetDualLedSmoothOn()


#This is for testing.
if __name__ == '__main__':

    led_port = [17, 27, 22, 23, 24, 25, 5, 6, 13, 19]
    Init_Led_Port(led_port)
