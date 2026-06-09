import sys
input = sys.stdin.readline

A, B = map(int, input().split())

answer = '0'

for i in range(A, B+1):
    if 1920%i==0 and 2880%i==0:
        answer = '1'
        break

print(answer)