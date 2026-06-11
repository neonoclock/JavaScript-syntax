import sys
input = sys.stdin.readline

N = int(input())

if N<=10:
    for i in range(1, N+1):
        for j in range(i):
            print('*', end = ' ')
        print()