import sys
input = sys.stdin.readline

sum_val = 0
cnt = 0

for i in range(1, 11):
    num = int(input())
    if num>0 and num<=200:
        cnt += 1
        sum_val += num
print(sum_val, round(sum_val/cnt, 1), end=' ')