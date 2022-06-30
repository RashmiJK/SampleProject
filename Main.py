#!/usr/bin/python3

import sys
import platform
from selenium import webdriver
from bs4 import  BeautifulSoup
import pandas as pd

def python_ver_in_use():
    print(sys.version)
    print(sys.executable)
    print('This is python version {}'.format(platform.python_version()))

def fibonacci( b = 1):
    #a, b = 0, 1
    a = 0
    while(b < 1000):
        print(b, end = ' ', flush = True)
        a, b = b, a + b
    print()

def data_types():
    x = [1, 'two', 3, 4, 'five'] # list, sqaure brackets, mutable, heterogenous elements
    x[2] = 'three'
    for i in x:
        print(f'i is {i}')
    #y = (1, 'two', 3, 4, 'five') # tuple, parenthesis, immutable
    y = tuple(range(5))
    print(type(y))
    for i in y:
        print(f'i is {i}')
    z = {'one': 1, 'two': 2, 'three': 3, 'four':4, 'five':5} # dictionary, key-value pair, mutable
    for k, v in z.items():
        print(f'{k} => {v}')
    p = [1,'two',3.0, [4,'four'],5]
    q = [1,'two',3.0, [4,'four'],5]
    q[1] = 2
    print('p is {}'.format(p))
    print('q is {}'.format(q))
    print(id(p[1]))
    print(id(q[1]))

#def web-s():
#    driver = webdriver.Chrome("/usr/lib/ch")


def main():
    print('Welcome to my program!')
    greet = ''' Choose your option as below?
    0 - To exit2
    1 - To check python version in use.
    2 - To print fibinacci numbers until 1000.
    3 - To examin diff b/w list, tuple and dict data types.
    4 - To scrape Amazon for chilli chopper

    '''
    while True :
        option = int(input(greet))
        if option == 0:
            break
        elif option == 1:
            python_ver_in_use()
        elif option == 2:
            fibonacci()
        elif option == 3:    
            data_types()
        else:
            print('not yet implemented')

if __name__ == '__main__':
    main()
