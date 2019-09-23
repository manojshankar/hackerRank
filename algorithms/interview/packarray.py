#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the packNumbers function below.
def packNumbers(arr):
    repCounter = 1
    newlist = []
    print(len(arr))
    arr.append(9999)
    print(len(arr))
    for i in range(len(arr)-1):
        if arr[i] == arr[i + 1]:
            repCounter += 1
        else:
            if repCounter > 1:
                newlist.append(str(arr[i]) + ":" + str(repCounter))
                repCounter = 1
            else:
                newlist.append(str(arr[i]))
    return newlist


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    res = packNumbers(arr)

    print('\n'.join(res))
