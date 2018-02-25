import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def my_callback(channel):
    print "Rising edge detected on port 24 - even though, in the main thread,"
    print "we are still waiting for a falling edge"

print "The orange button is the threaded callback"
raw_input("Press enter when ready")

GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)

try:
    print "Waiting for falling edge on port 23"
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print "Falling edge detected. Exiting"

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
