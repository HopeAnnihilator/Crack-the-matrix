#!/usr/bin/env python3

# importing numpy (a math program that does cool things)
# numpy needs to be installed with pip3 (pip3 install numpy)
import numpy as np
# importing time from python
import time 

# first value in dictionary when it is created, using a number for easy management later
trashable = 1
# empty dictionary
vadadoom = {}
# tell program to get current time to calculate how long it takes
start = time.time()

# encrypted text to crack, numpy is used to turn these lists into a matrix
EncodedMsg = np.array([
    [25, -33, -53],
    [27, -31, -84],
    [8, -23, 40],
    [-15, 15, 44],
    [6, -31, 107],
    [15, -30, 24]
])

# input test parameters when program started
size = input("Input matrix size as a total number of values in matrix: ")
depth = input("Range to test (positive integer): ")
print('\n\n\n')

# ensure that inputs will create a square matrix
try:
    # check that the inputs are numbers
    depth = int(depth)
    size = int(size)
    # verify the size input is the square of an integer by raising the size to the 1/2 power
    singularsize = int(size ** (1/2))
    if singularsize != size ** (1/2):
        exit()
except:
    # if anything fails print message and exit program
    print('use square numbers such as 3x3 matrix = 9, 4x4 = 16')
    exit()
# tell program how large the matrix is for later
myspot = size

# create the matrix with the minimum range for every value
for i in range(1, singularsize + 1):
    # create rows
    for i in range(1, singularsize + 1):
        # create the same number of columns by repeating instruction
        # setting each key in dictionary to minimum range
        vadadoom[trashable] = -depth
        # add one to the first dictionary key to have a new key
        trashable = trashable  + 1
# replace the 2 known numbers in matrix
vadadoom[1] = 1
vadadoom[6] = 3
# save original matrix to avoid duplicate output later and save time
previousprint = str(vadadoom)

# function to test keys and attempt to decode
def makekey():
    # declare the variable declared earlier in the program as global so it can be eddited freely
    global previousprint
    # create an empty, temporary list for each row of matrix
    tmplist = []
    # create an empty list for all rows of matrix
    fulllist = []
    # move to the first value in matrix
    x = 1
    # create the matrix
    for i in vadadoom.values():
        # for each key in the dictionary add that value to the temporary list
        tmplist.append(i)
        # move to the value in dictionary (once again why numbers used)
        x = x + 1
        # if the temporary list has the same amount of columns as the square matrix should have execute these instructions
        if x  > singularsize:
            # write the temporary list to the full list
            fulllist.append(tmplist)
            # set the temporary list to empty
            tmplist = []
            # move back to the first spot in temporary list
            x = 1
    # after the for loop is finished, use the full list to create a matrix using numpy
    key = np.array(fulllist)
    # have a switch to quickly skip executing if the inverse is a singular matrix
    flip = 0
    # attempt to create an inverse matrix
    try:
        inverse = np.linalg.inv(key)
    # if matrix is singular flip the switch
    except np.linalg.LinAlgError:
        flip = 1
    # if switch was not flipped run these instructions
    if flip == 0:
        # use the encryption algorithm to multiply the encrypted message by the inverse of key generated
        outputinverse = (EncodedMsg.dot(inverse))
        # for each row in the output execute this
        for line in outputinverse:
            # if switch is flipped break this loop
            if flip == 1:
                break 
            # for each column in the row execute this
            for item in line:
                # check if number is integer 
                # rounded back 3 points because float point errors are common in programs like this
                if round(item, 0) != round(item, 3):
                    # if any number is not an integer flip the switch and break the loop
                    flip = 1 
                    break
                # if all numbers are integers, round them to 0 places (float point errors once again)
                item = round(item, 0)
                # all values should be between 0 and 26 based off given info, test this
                if item < 0 or item > 26:
                    # if value is less than 0 or greater than 26, flip switch and break loop
                    flip = 1
                    break
    # if switch is flipped and key wasnt previously found, show the output!!!!
    if flip == 0 and previousprint != str(vadadoom):
        # obtain the current time
        now = time.time()
        # calculate how long program took to execute
        print('Found in: ' + str(round((now - start), 3)) + ' seconds\n')
        # print encryption key
        print('key')
        print(key)
        # print inverse of encryption key
        print('\ninverse')
        print(inverse)
        # print decoded message
        print('\ndecoded')
        print(outputinverse)
        print('\n')
        # save the current matrix to avoid duplicate output
        previousprint = str(vadadoom)
        # reset the text conversion
        text = []
        # for row in decoded matrix
        for value in outputinverse:
            # for column in row 
            for item in value:
                # convert values to integers
                item = int(item)
                # if item is 0 
                if item == 0:
                    # because the 0 character is \x00 (machine code) use character 160, which is space as defined by encryption algorithm
                    # write this space to the list of character conversion
                    text.append(chr(160))
                else:
                    # add 96 to every letter value (letters begin with a = 97, b =98 and so on) then convert to letters
                    # write the character to same list as above
                    text.append(chr(item + 96))
        # join the list of characters with nothing between and print
        print('Decoded Text: ' + ''.join(text).title())
        print('\n\n')
        # write each decoded message to text file (can also be written to list or dictionary or anything really)
        # i did not do this but this can be compared against wordlists to find the most likely correct solutions
        # create a file called "matrixMessages.txt" and/or append to it
        with open('matrixMessages.txt', 'a+') as f:
            # join text with nothing between before writing
            f.write(''.join(text) + '\r\n')
            # close text file
            f.close()


# create a loop that runs until program is killed
while True:
    # execute program to test key as the first instruction of each loop
    makekey()
    # attempt to run program
    try:
        # if program reaches a known value, skip to next value
        if myspot == 1 or myspot == 6:
            myspot = myspot - 1
        # if current value is greater than or equal to max value of range set it to the minimum value and move 1 spot forward in dictionary
        # this is why the keys are numbers, to make it easy to traverse them no matter what size the dictionary is
        elif vadadoom[myspot] >= depth:
            vadadoom[myspot] = -depth
            myspot = myspot -1
        # if current is not in the first 2 values and is not greater than the max range, add one to that value and move back to the last value in dictionary
        else:
            vadadoom[myspot] = vadadoom[myspot] + 1
            myspot = size
    # the first key is 1, if the program reaches 0 it will exit
    except KeyError:
        now = time.time()
        print('Program ran for: ' + str(round((now - start), 3)) + ' seconds\n')
        exit()


# correct outputs, program does not know these
# key inverse
# [[ -1. -10.  -8.]
#  [ -1.  -6.  -5.]
#  [ -0.  -1.  -1.]]
# decrypted 
# [[ 8.  1. 18.]
#  [ 4.  0. 23.]
#  [15. 18. 11.]
#  [ 0. 16.  1.]
#  [25. 19.  0.]
#  [15.  6.  6.]]
# key 
# [1, -2, 2],
# [-1, 1, 3],
# [1, -1, -4]