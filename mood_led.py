#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import threading


#LED Port Setting
led = [17, 27, 22, 23]
#led = [17, 27, 22, 23, 24, 25, 5, 6, 13, 19]


led_step = 0.0005
led_frequency = 0.023
led_loop_step = 45 # led_frequency / led_step - 1


#LED Mode
led_mode_on_off = 0
led_mode_off = 1
led_mode_on = 2



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



Threads = []
Threads_reverse = []


#
# Smoothly Turn on left to right LED
# and then Smoothly Turn off right to left it
#
def SetLedLeftTurn():

    for i in led:
        th = led_thread(i, led_mode_on_off)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(0.2)

    for th in Threads:
        th.join()


    led_reverse = led
    led_reverse.reverse()

    for i in led_reverse:
        th = led_thread(i, led_mode_on_off)
        Threads_reverse.append(th)

    for th in Threads_reverse:
        th.start()
        time.sleep(0.2)

    for th in Threads_reverse:
        th.finish()
        th.join()


#
# Smoothly Turn on right to left LED
# and then Smoothly Turn off left to right it
#
def SetLedRightTurn():

    led_reverse = led
    led_reverse.reverse()

    for i in led_reverse:
        th = led_thread(i, led_mode_on_off)
        Threads_reverse.append(th)

    for th in Threads_reverse:
        th.start()
        time.sleep(0.2)

    for th in Threads_reverse:
        th.finish()
        th.join()

    led_reverse.reverse()

    for i in led_reverse:
        th = led_thread(i, led_mode_on_off)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(0.2)

    for th in Threads:
        th.join()



#
# Smoothly Turn on left to right All LED
#
def SetLedLeftShiftOn():

    for i in led:
        th = led_thread(i, led_mode_on)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(0.3)

    for th in Threads:
        th.join()


#
# Smoothly Turn off left to right All LED
#
def SetLedLeftShiftOff():

    for i in led:
        th = led_thread(i, led_mode_off)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(0.2)

    for th in Threads:
        th.join()



#
# Smoothly Turn on right to left All LED
#
def SetLedRightShiftOn():

    led_reverse = led
    led_reverse.reverse()

    for i in led:
        th = led_thread(i, led_mode_on)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(0.2)

    for th in Threads:
        th.join()


#
# Smoothly Turn off right to left All LED
#
def SetLedRightShiftOff():

    led_reverse = led
    led_reverse.reverse()

    for i in led:
        th = led_thread(i, led_mode_off)
        Threads.append(th)

    for th in Threads:
        th.start()
        time.sleep(0.2)

    for th in Threads:
        th.join()



#
# Smoothly Turn Off  All LED
#
def SetLedSmoothOff():
    for i in led:
        th = led_thread(i, led_mode_off)
        Threads.append(th)

    for th in Threads:
        th.start()

    for th in Threads:
        th.finish()
        th.join()


#
# Smoothly Turn On  All LED
#
def SetLedSmoothOn():
    for i in led:
        th = led_thread(i, led_mode_on)
        Threads.append(th)

    for th in Threads:
        th.start()

    for th in Threads:
        th.finish()
        th.join()





#
# Turn On All LED
#
def SetLedOn():
    for k in led:
        GPIO.setup(k, GPIO.OUT)
        GPIO.output(k, True)

#
# Turn Off All LED
#
def SetLedOff():
    for k in led:
        GPIO.setup(k, GPIO.OUT)
        GPIO.output(k, False)






if __name__ == '__main__':
    
    GPIO.setmode(GPIO.BCM)
    for k in led:
        GPIO.setup(k, GPIO.OUT)
        GPIO.output(k, False)

    #SetLedMoving()
    #SetLedOn()
    #SetLedOn()
    #time.sleep(1)
    SetLedRightTurn()
