#!/usr/bin/env python3

import numpy as np
import time
import msgpack as mp
import msgpack_numpy as mpn

start = time.time()
EncodedMsg = np.array([
    [25, -33, -53],
    [27, -31, -84],
    [8, -23, 40],
    [-15, 15, 44],
    [6, -31, 107],
    [15, -30, 24]
])

def makekey(inverse):  
    flip = 0
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
        now = time.time()
        print('Found in: ' + str(round((now - start), 3)) + ' seconds')
        print('Key')
        print(np.linalg.inv(inverse))
        print('Inverse')
        print(inverse)
        print('Decoded Matrix')
        print(outputinverse)
        print('Decoded Text: ' + str(''.join(text).title()))
        print('\n')


with open('zelistofinverses', 'rb') as f:
    inverselist = mp.unpack(f, object_hook = mpn.decode)
for inverse in inverselist:
    makekey(inverse = inverse)



now = time.time()
print('Program ran for: ' + str(round((now - start), 3)) + ' seconds\n')