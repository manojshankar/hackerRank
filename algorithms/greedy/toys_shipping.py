#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the toys function below.
def toys(w):
    count = 0
    w.sort()
    range_c = 0
    for ele in w:
        if ele > range_c:
            count += 1
            range_c = ele + 4
    return count


if __name__ == '__main__':
    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    print(result)
