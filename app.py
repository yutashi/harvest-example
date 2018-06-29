#!/usr/bin/env python3
import requests
import random
import time
import sys


def get_temp():
    return random.randint(0, 50)


if __name__ == '__main__':
        print('{"humidity": {}}'.format(get_temp()))
        time.sleep(30)
