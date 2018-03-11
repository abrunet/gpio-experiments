import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def rgb(red, green, blue):
    GPIO.output(21, GPIO.LOW if not red else GPIO.HIGH)
    GPIO.output(20, GPIO.LOW if not green else GPIO.HIGH)
    GPIO.output(16, GPIO.LOW if not blue else GPIO.HIGH)

    if red and not blue and not green:
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)

def my_callback(channel):
    rgb(False, False, True)
    time.sleep(1)
    rgb(False, True, True)
    time.sleep(1)
    rgb(False, True, False)
    time.sleep(1)
    rgb(True, True, False)
    time.sleep(1)
    rgb(True, False, False)
    time.sleep(1)
    rgb(True, False, True)
    time.sleep(1)
    rgb(True, True, True)
    time.sleep(1)
    rgb(False, False, False)

GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback, bouncetime=300)

try:
    GPIO.wait_for_edge(23, GPIO.FALLING)
    rgb(False, False, False)
    print "See ya!"

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
