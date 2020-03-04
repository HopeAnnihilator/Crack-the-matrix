#!/usr/bin/env python3

import numpy as np
import time

EncodedMsg = np.array([
    [25, -33, -53],
    [27, -31, -84],
    [8, -23, 40],
    [-15, 15, 44],
    [6, -31, 107],
    [15, -30, 24]
])

matrix = []

size = input("Input matrix size as a total number of values in matrix: ")
depth = input("Range to test (positive integer): ")
print('\n\n\n')
start = time.time()

try:
    depth = int(depth)
    size = int(size)
    singularsize = int(size ** (1/2))
    if singularsize != size ** (1/2):
        exit()
except:
    print('use square numbers such as 3x3 matrix = 9, 4x4 = 16')
    exit()

badlist = []
previoustext = str('a')
x = singularsize
y = x
for i in range(0, size):
    matrix.append(-depth)
matrix[0] = 1
badlist.append(2)
matrix[5] = 3
badlist.append(137)
matrix = np.array_split(matrix, 3)

def makekey():  
    global previoustext
    flip = 0
    try:
        inverse = np.linalg.inv(matrix)
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
    if flip == 0:
        text = []
        for value in outputinverse:
            for item in value:
                item = int(item)
                if item == 0:
                    text.append(chr(160))
                else:
                    text.append(chr(item + 96))
        newtext = str(''.join(text).title())
        if newtext != previoustext:
            previoustext = newtext
            now = time.time()
            print('Found in: ' + str(round((now - start), 3)) + ' seconds')
            print('Key')
            print(np.array(matrix))
            print('Inverse')
            print(inverse)
            print('Decoded Matrix')
            print(outputinverse)
            print('Decoded Text: ' + newtext)
            print('\n')


def movespot():
    global x, y
    if y > 1:
        y = y - 1
    else:
        y = singularsize
        x = x - 1

makekey()
while x > 0:
    location = x ** 7 + y ** 2
    value = matrix[x - 1][y - 1]
    if location in badlist:
        movespot()
    elif value >= depth:
        matrix[x - 1][y - 1] = -depth
        movespot()
    else:
        matrix[x - 1][y - 1] = value + 1
        makekey()
        x = singularsize
        y = singularsize

now = time.time()
print('Program ran for: ' + str(round((now - start), 3)) + ' seconds\n')
