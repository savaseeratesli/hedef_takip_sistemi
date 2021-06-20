import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
try:
  i=0
  while (i<1):
    p.ChangeDutyCycle(4)
    time.sleep(1)
    p.ChangeDutyCycle(12)
    time.sleep(1)
    p.ChangeDutyCycle(4)
    time.sleep(1)
    i+=1
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()