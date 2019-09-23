#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'employeeWithLesserThanKBreaks' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY employeeCalls
#  2. INTEGER k
#

def employeeWithLesserThanKBreaks(employeeCalls, k):
    # Write your code here
    res = []
    emp = dict()
    for i in employeeCalls:
        if i[0] in emp.keys():
            if i[1] > emp[i[0]][0]:
                emp[i[0]] = [i[2], emp[i][1] + 1]
        else:
            emp[i[0]] = [i[2], 1]
    print(emp)
    return res


if __name__ == '__main__':
    employeeCalls_rows = int(input().strip())
    employeeCalls_columns = int(input().strip())

    employeeCalls = []

    for _ in range(employeeCalls_rows):
        employeeCalls.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    result = employeeWithLesserThanKBreaks(employeeCalls, k)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
