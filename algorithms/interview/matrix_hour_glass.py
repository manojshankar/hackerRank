"""
2D Array - DS
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    maximum = -7 * 9
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            tsum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +\
                   arr[i + 1][j + 1] +\
                   arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if tsum > maximum:
                maximum = tsum
    return maximum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
