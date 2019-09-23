#!/bin/python3

"""
Problem statement : https://www.hackerrank.com/challenges/angry-children

"""
import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    result = 100000000000000000000
    n = len(arr)
    for i in range(n - k + 1):
        result = int(min(result, arr[i + k - 1] - arr[i]))

    return result


if __name__ == '__main__':
    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)
