
import sys

#LOG_FILE = sys.stdout
LOG_FILE = '/home/pi/pi-coffee/coffee.log'

def clear_log():
    if type(LOG_FILE) is str:
        with open(LOG_FILE, 'w') as f:
            f.write('')

def printd(text):
    if type(LOG_FILE) is str:
        f = open(LOG_FILE, 'a')
    else:
        f = LOG_FILE
    print >> f, text

