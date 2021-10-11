# Domino Disaster
# https://codeforces.com/contest/1567/problem/A

import sys

test_case = int(input())

for _ in range (test_case):
    n = int(input())
    arr = list(map(str, input()))
    for i in range(len(arr)):
        if arr[i] == 'U':
            sys.stdout.write('D')
        elif arr[i] == 'D':
            sys.stdout.write('U')
        else:
            sys.stdout.write(arr[i])
    sys.stdout.write("\n")