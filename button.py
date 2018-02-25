import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

raw_input("Press enter when ready")

print "Waiting for edge on port 23"

try:
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print "Falling edge detected"
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
