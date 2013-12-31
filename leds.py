import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)


def flash_led(led_to_flash):
    
    i = 0
    while i <= 5:
        
        if i % 2 == 0:
            GPIO.output(led_to_flash, True)
        else:
            GPIO.output(led_to_flash, False)

        i += 1
        time.sleep(1)

    GPIO.output(led_to_flash, False)


def flash_green():
    flash_led(GREEN_LED)


def flash_red():
    flash_led(RED_LED)
