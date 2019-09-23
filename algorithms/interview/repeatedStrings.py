#!/bin/python3
"""
Repeated String
https://www.hackerrank.com/challenges/repeated-string/problem
"""


import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    acount = 0
    for x in s:
        if x == 'a':
            acount += 1
    count = acount * (n // len(s))
    if n % len(s) != 0:
        rem_index = n % len(s)
        for i in range(rem_index):
            if s[i] == 'a':
                count += 1
    return count


if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
