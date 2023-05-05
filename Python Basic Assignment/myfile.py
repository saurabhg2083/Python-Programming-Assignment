import multiprocessing
import time
import sys
from datetime import datetime
from time import sleep
import random

def printsec(seconds):
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())

if __name__ == '__main__':
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=printsec, args=(seconds,))
        proc.start()