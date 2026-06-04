import sys
input = sys.stdin.readline

N = int(input())
sum_val = 0

for i in range(1, N + 1):
    num = int(input())

    if num % 2 == 1 and num % 3 == 0:
        sum_val += num

print(sum_val)