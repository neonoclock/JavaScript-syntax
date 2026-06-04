import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0

sum_val = 0

for i in range(A, B+1):
    if i%5==0 or i%7==0:
        cnt += 1
        sum_val += i
print(sum_val, round(sum_val/cnt, 1), end=' ')