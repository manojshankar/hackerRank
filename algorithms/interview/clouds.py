#!/bin/python3
"""
Jumping on the Clouds
https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""


import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
# 1 0 0 0 0 1 0 1 0

def jumpingOnClouds(c):
    jump = 0
    i = 0
    while i < (len(c) - 1):
        if c[i] == 1:
            i += 1
            jump += 1
        if i < len(c) - 1 and c[i] == 0:
            i += 2
            jump += 1
    return jump


if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
