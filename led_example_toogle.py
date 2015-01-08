import RPi.GPIO as GPIO
import time

# CONSTANTS
LED_PIN = 11
TOGGLE_SLEEP = 0.5 

# INITIALIZATION
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

print "Press CTRL+C to quite"
# PROGRAM
try:
	while 1:
		# Take the LED on
		GPIO.output(LED_PIN, GPIO.HIGH)

		# Wait 100 ms
		time.sleep(TOGGLE_SLEEP)

		# Take the LED off
		GPIO.output(LED_PIN, GPIO.LOW)

		# Warte 100 ms
		time.sleep(TOGGLE_SLEEP)
except KeyboardInterrupt:
	print "Exit"

GPIO.output(LED_PIN, GPIO.LOW)

