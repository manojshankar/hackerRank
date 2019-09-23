#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    visited = {k: False for k in range(n)}
    print(visited)

    # Initialize result
    swap_count = 0
    for i in range(n):
        cycle_s = 0
        j = i
        while not visited[j]:
            # mark node as visited
            visited[j] = True

            # move to next node
            j = arr[j] - 1
            cycle_s += 1

        if cycle_s > 0:
            swap_count += (cycle_s - 1)
            # return answer
    return swap_count


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)
