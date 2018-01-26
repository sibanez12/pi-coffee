
import sys, os
from card_reader import CardReader

CARDS_FILE = 'cards.csv'

def main():
    card_reader = CardReader()
    card_num = card_reader.read_card()
    name = raw_input('Enter name: ')
    with open(CARDS_FILE, 'a') as f:
        f.write('{}, {}\n'.format(card_num, name))


if __name__ == '__main__':
    main()

