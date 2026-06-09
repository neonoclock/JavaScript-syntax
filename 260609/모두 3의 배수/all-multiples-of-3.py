import sys
input = sys.stdin.readline

answer = '1'

for i in range(1, 6):
    N = int(input())
    if N % 3 ==0:
        continue
    if N % 3 !=0:
        answer = '0'
        break

print(answer)