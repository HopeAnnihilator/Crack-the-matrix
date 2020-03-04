#!/usr/bin/env python3
# making easier to execute for linux users

# importing numpy (a math program that does cool things)
# numpy needs to be installed with pip3 (pip3 install numpy)
import numpy as np
# importing time from python
import time 

# encrypted text to crack, numpy is used to turn these lists into a matrix
EncodedMsg = np.array([
    [25, -33, -53],
    [27, -31, -84],
    [8, -23, 40],
    [-15, 15, 44],
    [6, -31, 107],
    [15, -30, 24]
])

# define an empty list to create matrix with
matrix = []
# create list for locations that will be avoided
badlist = []

# input test parameters when program started
size = input("Input matrix size as a total number of values in matrix: ")
depth = input("Range to test (positive integer): ")
print('\n\n\n')

# tell program to get current time to calculate how long it takes
start = time.time()

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

# define x and y as largest values on the matrix grid
x = singularsize
y = x

# create the matrix
for i in range(0, size):
    matrix.append(-depth)

# change known values and add their locations to badlist
matrix[0] = 1
badlist.append(2)
matrix[5] = 3
badlist.append(137)

# splice the matrix into square
matrix = np.array_split(matrix, singularsize)

# function to test keys and attempt to decode
def makekey():  
# have a switch to quickly skip executing if the inverse is a singular matrix
    flip = 0
    # attempt to create an inverse matrix
    try:
        inverse = np.linalg.inv(matrix)
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
    if flip == 0:
        # obtain the current time
        now = time.time()
        # calculate how long program took to execute
        print('Found in: ' + str(round((now - start), 3)) + ' seconds\n')
        # print encryption key
        print('key')
        print(np.array(matrix))
        # print inverse of encryption key
        print('\ninverse')
        print(inverse)
        # print decoded message
        print('\ndecoded')
        print(outputinverse)
        print('\n')
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


# traverse the matrix grid
def movespot():
    # declare variables global so entire program can use the changed values
    global x, y
    # if not in the final column, move 1 column left
    if y > 1:
        y = y - 1
    # if final column reached
    else:
        # return to far right column
        y = singularsize
        # move up 1 row
        x = x - 1

# loop for while not at end of list
while x > 0:
    # define location using the sum of x to a prime and y square to save time
    location = x ** 7 + y ** 2
    # find value at current location beforehand to save time 
    value = matrix[x - 1][y - 1]
    # check if location can be changed, if not, skip it 
    if location in badlist:
        movespot()
    # check if current value is greater than max value and if so, set to the min range then move to next location
    elif value >= depth:
        # check for possible key
        makekey()
        matrix[x - 1][y - 1] = -depth
        movespot()
    # if value is not greater than max and allowed to be changed
    else:
        # check for possible key
        makekey()
        # add 1 to value 
        matrix[x - 1][y - 1] = value + 1
        # move to the last value in list
        x = singularsize
        y = singularsize

# print total time to run program
now = time.time()
print('Program ran for: ' + str(round((now - start), 3)) + ' seconds\n')