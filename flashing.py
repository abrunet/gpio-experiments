import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 2)
current_duty_cycle = 0
pwm.start(current_duty_cycle)

def my_callback(channel):
    global pwm, current_duty_cycle
    current_duty_cycle = 50 if current_duty_cycle == 0 else 0
    pwm.ChangeDutyCycle(current_duty_cycle)

print "The orange button is the light switch"

GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback, bouncetime=300)

try:
    print "Waiting for black button to exit program\n"
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print "Exiting"
    pwm.stop()

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
