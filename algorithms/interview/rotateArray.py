#!/bin/python3

import os
"""
Arrays: Left Rotation
Arrays: Left Rotation
"""

# Complete the rotLeft function below.
def rotLeft(a, d):
    alen = len(a)
    rotate_index = d if d < alen else alen - (d % alen)

    s = []
    for i in range(rotate_index, len(a)):
        s.append(a[i])
    for i in range(rotate_index):
        if i == rotate_index - 1:
            s.append(a[i])
        else:
            s.append(a[i])
    return s


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)
