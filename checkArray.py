#!/usr/local/bin/python3.8
import os, sys

#find a missing number from 1 to x in a given array
def checkMissing():
    someArray = [1,2,3,11,5,6,7,12,9,10,4]

    num = 1

    someArray.sort()

    for x in someArray:

        if x > num:
            num+=1
            print(x)
        else:
            print("missing {}".format(num))
            break

#max and mininum element in a given array
def maxAndMinElement():
    someArray = [1,2,3,11,5,6,7,12,9,10,4,12]

    max = 0
    min = None

    for x in someArray:

        if min == None:
            min = x

        if x > max:
            max = x
            #print(x)
        elif x <= min:
            min = x
            #print(x)
        else:
            continue
        print("Update! Max = {}, Min = {}".format(max,min))

def getNumInput():
    try:
        someNum = int(input("Enter number:"))
    except ValueError:
        print("Not a valid number:")
    return someNum

#pair of numbers that match the sum of a given number
def matchSum():

    compSum = getNumInput()
    someArray = [1,2,3,11,5,6,7,12,9,10,4]

    for x in someArray:
        for y in someArray:
            sum = x + y

            if  sum == compSum:
                print("{} equal the sum of array elements {} and {}:".format(compSum,x,y))

getNumInput()
