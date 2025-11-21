from time import sleep as sl
from os import system as sys
from datetime import datetime as d_time


def get_time():
    h = int(input("Enter hours:"))
    m = int(input("Enter minutes:"))
    sec = int(input("Enter seconds:"))
    total = h * 3600 + m * 60 + sec
    return total


def delay():
    for i in range(3, 0, -1):
        print(i, end='..' if i > 1 else '\n')
        sl(1)


while True:
    x = input('Timer app\n1)start timer\t2)stopwatch\t  3)exit timer\n')

    if x == '1':
        z = get_time()
        delay()
        while z >= 1:
            print(f'{z}s            {d_time.now():real time _%H:%M:%S_}')
            sl(1)
            z -= 1
            sys('clear')

    elif x == '2':
        z = get_time()
        delay()
        i = 0
        while i < z:
            print(f'{i + 1}s        {d_time.now():real time _%H:%M:%S_}')
            sl(1)
            sys('clear')
            i += 1

    elif x == '3':
        print('Exiting',end = '')
        sl(0.25)
        for i in range(3):
            print('.',end='')
            sl(0.25)
        break

    else:
        print('Invalid input')
