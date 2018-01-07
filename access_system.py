
import sys, os
import time
import RPi.GPIO as GPIO

from card_reader import CardReader
from utils import clear_log, printd


OUT_PIN = 7
UNLOCK_TIME = 3 # seconds


class AccessSystem(object):
    def __init__(self, cards_file):
        clear_log()
        self.card_reader = CardReader()
        self.cards_file = cards_file
        # Use RPi pin numbering
        GPIO.setmode(GPIO.BOARD)
        # setup output pin
        GPIO.setup(OUT_PIN, GPIO.OUT)
        GPIO.setwarnings(False)

    def run_access_control(self):
        printd('Starting access control system ...')
        while True:
            # read RFID card reader
            card_num = self.card_reader.read_card()
            # read cards file
            cards_dic = self._read_cards_file()
            # check permission
            if card_num in cards_dic.keys():
                name = cards_dic[card_num]
                self._grant_access(name)
            elif card_num is not None:
                self._deny_access(card_num)


    def _read_cards_file(self):
        cards_dic = {}
        with open(self.cards_file) as f:
            for line in f:
                line_vals = [s.strip() for s in line.split(',')]
                if len(line_vals) != 2:
                    printd('ERROR: invalid line in cards file: {}'.format(line))
                else:
                    try:
                        num = int(line_vals[0])
                        name = line_vals[1]
                    except ValueError as e:
                        printd('ERROR: invalid card number on line: {}'.format(line))
                    cards_dic[num] = name
        return cards_dic


    def _grant_access(self, name):
        printd('Access Granted for {}'.format(name))
        GPIO.output(OUT_PIN, True)
        time.sleep(UNLOCK_TIME)
        GPIO.output(OUT_PIN, False)


    def _deny_access(self, num):
        printd('Access Denied for card: {}'.format(num))
        GPIO.output(OUT_PIN, False)


def main():
    clear_log()
    acSys = AccessSystem('cards.csv')
    try:
        acSys.run_access_control()
    except:
        GPIO.cleanup()
        printd('Finished cleaning up ... Done.')

if __name__ == '__main__':
    main()




