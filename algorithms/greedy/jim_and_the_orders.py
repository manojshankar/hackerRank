#!/bin/python3

"""
Problem statement : https://www.hackerrank.com/challenges/jim-and-the-orders

"""
import math
import os
import random
import re
import sys


# Complete the jimOrders function below.
def jimOrders(orders):
    # calculate serve time for each order and create dict
    sevTime = {}
    index = 1
    for order in orders:
        key = order[0] + order[1]
        if key in sevTime:
            sevTime[key] = [sevTime[key], index]
        else:
            sevTime[key] = index
        index += 1
    deliver = []
    for key in sorted(sevTime.keys()):
        deliver.append(sevTime[key])
    out = []
    flatten(deliver, out)
    return out


def flatten(items, output):
    for i in items:
        if type(i) == list:
            flatten(i, output)
        else:
            output.append(i)


if __name__ == '__main__':

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    print(result)
