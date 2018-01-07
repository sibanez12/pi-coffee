
import evdev
import sys, os

from utils import printd

class CardReader(object):
    def __init__(self):
        # find the RFID card reader device
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

        rfid_devs = [d for d in devices if 'RFID' in d.name]
        if len(rfid_devs) == 0:
            printd('ERROR: No RFID devices found... exiting')
            sys.exit(1)

        self.rfid_dev = rfid_devs[0]

        if len(rfid_devs) > 1:
            printd('WARNING: Multiple RFID devices found... using: {}'.format(self.rfid_dev.name))


    def read_card(self):
        # lock the device
        self.rfid_dev.grab()
        # read the digits
        digits = []
        for event in self.rfid_dev.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                data = evdev.categorize(event)
                if data.keycode == 'KEY_ENTER':
                    break
                if data.keystate == 1: # the key is pressed down
                    digits.append(data.keycode.replace('KEY_', ''))
        # unlock the device
        self.rfid_dev.ungrab()
        input_str = ''.join(digits)
        try:
            card_num = int(input_str)
            return card_num
        except ValueError as e:
            card_num = -1
            if input_str != '':
                printd('ERROR: Invalid card number entered: {}'.format(input_str))






