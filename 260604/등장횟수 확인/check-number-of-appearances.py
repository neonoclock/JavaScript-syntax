import sys
input = sys.stdin.readline

cnt_even = 0

for i in range(1, 6):
    num = int(input())
    if num%2 == 0:
        cnt_even += 1
print(cnt_even)