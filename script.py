#!/usr/bin/env python3

import numpy as np
import math
import time

global key 

trashable = 1
vadadoom = {}
fulllist = []
tmplist = []
key = 0

# EncodedMsg = np.array([
#                 [25, -33, -53, 27, -31, -84, 8, -23, 40],
#                 [-15, 15, 44, 6, -31, 107, 15, -30, 24]
#                 ])
EncodedMsg = np.array([
                [25, -33, -53, 27, -31, -84], 
                [8, -23, 40, -15, 15, 44],
                [6, -31, 107, 15, -30, 24]
                ])
# EncodedMsg = np.array([
#                 [33, 29],
#                 [69, 65],
#                 ])
# size = input("Input matrix size as a total number of values in matrix: ")
# depth = input("Range to test (positive integer): ")
size = 9
depth = 10

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

def makekey():
    global tmplist, key
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
    try:
        outputinverse = []
        inverse = []
        try:
            inverse = np.linalg.inv(key)
            outputinverse = (inverse.dot(EncodedMsg))
        except:
            pass
        output = key.dot(EncodedMsg)
        flipinverse = 0
        flip = 0
        for line in outputinverse: 
            for item in line:
                if round(item, 0) != round(item, 1):
                    flipinverse = 1 
                    break
                item = round(item, 0)
                if item < 0 or item > 26:
                    flipinverse = 1
                    break
        for line in output: 
            for item in line:
                if round(item, 0) != round(item, 1):
                    flip = 1 
                    break
                item = round(item, 0)
                if item < 0 or item > 26:
                    flip = 1
                    break
        if flipinverse == 0 and inverse:
            print(inverse)
            print(outputinverse)
            print('\n')
        if flip == 0:
            print(key)
            print(output)
            print('\n')

    except np.linalg.LinAlgError:
        key = 0

while vadadoom[1] <= depth:
    while True:
        makekey()
        try:
            if vadadoom[myspot] >= depth:
                vadadoom[myspot] = -depth
                myspot = myspot -1
            else:
                vadadoom[myspot] = vadadoom[myspot] + 1
                myspot = size
        except KeyError:
            exit()

