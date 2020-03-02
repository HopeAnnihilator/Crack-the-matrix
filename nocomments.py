#!/usr/bin/env python3

import numpy as np
import time 

trashable = 1
vadadoom = {}
start = time.time()

EncodedMsg = np.array([
    [25, -33, -53],
    [27, -31, -84],
    [8, -23, 40],
    [-15, 15, 44],
    [6, -31, 107],
    [15, -30, 24]
])


size = input("Input matrix size as a total number of values in matrix: ")
depth = input("Range to test (positive integer): ")
print('\n\n\n')


try:
    depth = int(depth)
    size = int(size)
    singularsize = int(size ** (1/2))
    if singularsize != size ** (1/2):
        exit()
except:
    print('use square numbers such as 3x3 matrix = 9, 4x4 = 16')
    exit()
myspot = size


for i in range(1, singularsize + 1):
    for i in range(1, singularsize + 1):
        vadadoom[trashable] = -depth
        trashable = trashable  + 1
vadadoom[1] = 1
vadadoom[6] = 3
previousprint = str(vadadoom)


def makekey():
    global previousprint  
    tmplist = [] 
    fulllist = []
    x = 1
    for i in vadadoom.values():
        tmplist.append(i)
        x = x + 1
        if x  > singularsize:
            fulllist.append(tmplist)
            tmplist = []
            x = 1
    key = np.array(fulllist)
    flip = 0
    try:
        inverse = np.linalg.inv(key)
    except np.linalg.LinAlgError:
        flip = 1
    if flip == 0: 
        outputinverse = (EncodedMsg.dot(inverse))
        for line in outputinverse:
            if flip == 1:
                break 
            for item in line:
                if round(item, 0) != round(item, 3):
                    flip = 1 
                    break
                item = round(item, 0)
                if item < 0 or item > 26:  
                    flip = 1
                    break
    if flip == 0 and previousprint != str(vadadoom):
        now = time.time()
        print('Found in: ' + str(round((now - start), 3)) + ' seconds\n')
        print('key')
        print(key)
        print('\ninverse')
        print(inverse)
        print('\ndecoded')
        print(outputinverse)
        print('\n')
        previousprint = str(vadadoom)
        text = []
        for value in outputinverse:
            for item in value:
                item = int(item)
                if item == 0:
                    text.append(chr(160))
                else:
                    text.append(chr(item + 96))
        print('Decoded Text: ' + ''.join(text).title())
        print('\n\n')
        with open('matrixMessages.txt', 'a+') as f:
            f.write(''.join(text) + '\r\n')



while True:
    makekey()
    try:
        if myspot == 1 or myspot == 6:
            myspot = myspot - 1
        elif vadadoom[myspot] >= depth:
            vadadoom[myspot] = -depth
            myspot = myspot -1
        else:
            vadadoom[myspot] = vadadoom[myspot] + 1
            myspot = size
    except KeyError:
        now = time.time()
        print('Program ran for: ' + str(round((now - start), 3)) + ' seconds\n')
        exit()