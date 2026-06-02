import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A>B:
    while A>=B:
        print(A, end=' ')
        A-=1
else:
    while B>=A:
        print(B, end=' ')
        B-=1