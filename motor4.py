#motor4.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# set pins as output
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

# spin motor one way for 10 seconds
GPIO.output(21,True)
GPIO.output(22,False)
time.sleep(10.0)
print ("first spin, 21 True")

# stop the motors for 1 second
GPIO.output(21,False)
GPIO.output(22,False)
time.sleep(1.0)
print ("first stop")

# spin motor the other way for 10 seconds
GPIO.output(21,False)
GPIO.output(22,True)
time.sleep(10.0)
print ("second spin, 22 True")

# stop the motors
GPIO.output(21,False)
GPIO.output(22,False)
print ("second stop")

GPIO.cleanup()
