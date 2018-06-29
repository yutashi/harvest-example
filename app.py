#!/usr/bin/env python3
import requests
import random
import time
import sys
import json
import os


def get_temp():
    return random.randint(0, 50)


print(os.environ['SOME_API'])
if __name__ == '__main__':
        print(json.dumps({'humidity': get_temp()}))
        time.sleep(30)
