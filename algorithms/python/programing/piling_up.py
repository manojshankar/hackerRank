#!/bin/python3

"""
Problem : https://www.hackerrank.com/challenges/piling-up/problem
"""
def is_stackble(arr):
    x, y = 0, len(arr)-1
    base = arr[0] if arr[0] >= arr[y] else arr[y]
    while x < y > 0:
        if arr[x] > base or arr[y] > base:
            return "No"
        if arr[y] <= arr[x] <= base:
            base = arr[x]
            x += 1
        elif arr[y] <= base:
            base = arr[y]
            y -= 1
    return "Yes"


if __name__ == '__main__':

    n = int(input())
    data = []
    for _ in range(n):
        ln = int(input())
        data.append(list(map(int, input().rstrip().split())))
    for i in data:
        print(is_stackble(i))
