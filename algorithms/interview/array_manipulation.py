#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    maximum = 0
    a = [0 for i in range(n)]
    for q in queries:
        a[q[0]] += q[2]
        if q[1] != n - 1:
            a[q[1] + 1] -= q[2]
    print(a)
    for i in range(1, n):
        a[i] += a[i - 1]
    print(a)
    for x in a:
        if x > maximum:
            maximum = x
    return maximum


def add(arr, N, lo, hi, val):
    arr[lo] += val
    if hi != N - 1:
        arr[hi + 1] -= val

    # Utility method to get actual


# array from operation array
def updateArray(arr, N):
    # convert array into prefix sum array
    for i in range(1, N):
        arr[i] += arr[i - 1]

    # method to print final updated array


def printArr(arr, N):
    updateArray(arr, N)
    for i in range(N):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result))
    arr = [0 for i in range(n)]
    for q in queries:
        add(arr, n, q[0],q[1],q[2])
    printArr(arr,n)
