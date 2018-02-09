#!/usr/bin/env python

import time
import subprocess
import os

def write_ip(ip):
    os.system('echo "{}" | ssh sibanez@netfpga2 "cat > /home/sibanez/pi-coffee/pi-coffee-ip.txt"'.format(ip))


curr_ip = subprocess.check_output('ifconfig | grep inet', shell=True)
write_ip(curr_ip)

while True:
    ip = subprocess.check_output('ifconfig | grep inet', shell=True)
    if ip != curr_ip:
        curr_ip = ip
        write_ip(curr_ip)
    time.sleep(900)

