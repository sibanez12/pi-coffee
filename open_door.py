
import time
import RPi.GPIO as GPIO

OUT_PIN = 7
UNLOCK_TIME = 4 # seconds

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(OUT_PIN, GPIO.OUT)
    GPIO.output(OUT_PIN, True)
    time.sleep(UNLOCK_TIME)
    GPIO.output(OUT_PIN, False)

if __name__ == '__main__':
    main()

