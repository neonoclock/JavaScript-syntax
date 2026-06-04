import sys
input = sys.stdin.readline

N = int(input())
sum_val = 0

for i in range(1, N+1):
    num = int(input())
    sum_val += num
print(sum_val, round(sum_val/N, 1), end=' ')