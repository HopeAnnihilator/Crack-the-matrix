#!/usr/bin/env python3

import numpy as np
import time
import msgpack as mp
import msgpack_numpy as mpn

start = time.time()
depth = 4
size = 9
listlen = 3
x = listlen
y = listlen
matrix = []
for i in range(0, size):
    matrix.append(-depth)
matrix[0] = 1
matrix[5] = 3

matrix = np.array_split(matrix, 3)
inverselist = []
keylist = []
badlist = [137, 2]
fictionary = {}
def makekey():  
    try:
        inverse = np.linalg.inv(matrix)
        inverselist.append(inverse)
        keylist.append(matrix)
    except np.linalg.LinAlgError:
        pass

def movespot():
    global x, y
    if y > 1:
        y = y - 1
    else:
        y = listlen
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
        x = 3
        y = 3

fictionary['keys'] = keylist
fictionary['inverses'] = inverselist
with open('zelistofinverses', 'wb+') as f:
    mp.pack(fictionary, f, default = mpn.encode)
now = time.time()
print('Program ran for: ' + str(round((now - start), 3)) + ' seconds\n')
