#!/usr/bin/env python3
import requests
import random
import time
import sys


def get_temp():
    return random.randint(0, 50)


if __name__ == '__main__':
    while True:
        try:
            requests.post("http://localhost:8880/deliver",
			      params={"soracom": "harvest"},
			      json={"temperature": get_temp()})
        except:
            print(sys.exc_info())

        time.sleep(60)
