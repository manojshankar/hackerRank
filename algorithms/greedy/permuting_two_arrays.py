#!/bin/python3

"""
problem statement at https://www.hackerrank.com/challenges/two-arrays/problem
"""

import math
import os
import random
import re
import sys


# Complete the twoArrays function below.
def twoArrays(k, A, B):
    # First find the minimum number of elements required for each each element in array B , which is required to
    # satisfy the condition A'[i] + B'[i] >= K
    min_arr = {}
    for i in B:
        if k - i in min_arr.keys():
            min_arr[k - i] += 1
        else:
            min_arr[k - i] = 1

    # check in A, if each element meets the requirement of min_arr
    ava_element = {}
    for x in A:
        for y in min_arr.keys():
            if x >= y:
                if y in ava_element.keys():
                    ava_element[y] += 1
                else:
                    ava_element[y] = 1
    # if number of available element is more that required number of elements for each value
    for j in min_arr.keys():
        element = ava_element.get(j, 0)
        if element == 0 or min_arr[j] > ava_element[j]:
            return "NO"
    return "YES"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        print(result)
