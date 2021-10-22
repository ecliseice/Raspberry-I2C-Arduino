import struct

import smbus
import time
import os

bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04


def request_reading():
    reading = bus.read_byte(SLAVE_ADDRESS)
    print(reading)


while True:
    request_reading()
    time.sleep(1)
    # command = input("Enter command: 1 - toggle LED, 2 - read A0 ")
    # if command == '1':
    #     bus.write_byte(SLAVE_ADDRESS, ord('l'))
    # elif command == '2':
    #     request_reading()