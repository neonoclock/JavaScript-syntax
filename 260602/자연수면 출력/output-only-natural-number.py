import sys
input = sys.stdin.readline

A,B = map(int, input().split())

if A>0:
    for i in range(B):
        print(A, end='')
else:
    print(0)