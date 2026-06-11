import sys
input = sys.stdin.readline

N = int(input())

if N <= 10:
    for i in range(N, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print()