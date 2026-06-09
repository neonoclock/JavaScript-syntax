import sys
input = sys.stdin.readline

N = int(input())

answer = 'N'

for i in range(2, N):
    if N % i ==0:
        answer = 'C'
        break
print(answer)