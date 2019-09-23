#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingReservations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY firstReservationList
#  2. 2D_INTEGER_ARRAY secondReservationList
#

def missingReservations(firstReservationList, secondReservationList):
    # Write your code here
    res = []
    lookup = dict()
    for i in firstReservationList:
        lookup[i[0]] = 1

    for i in secondReservationList:
        if i[0] not in lookup.keys():
            res.append(i)
    res.sort(key=lambda x: x[0])
    return res


if __name__ == '__main__':

    firstReservationList_rows = int(input().strip())
    firstReservationList_columns = int(input().strip())

    firstReservationList = []

    for _ in range(firstReservationList_rows):
        firstReservationList.append(list(map(int, input().rstrip().split())))

    secondReservationList_rows = int(input().strip())
    secondReservationList_columns = int(input().strip())

    secondReservationList = []

    for _ in range(secondReservationList_rows):
        secondReservationList.append(list(map(int, input().rstrip().split())))

    result = missingReservations(firstReservationList, secondReservationList)

    print('\n'.join(map(str, result)))
