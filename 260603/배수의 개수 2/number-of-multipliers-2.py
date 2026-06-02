import sys
input = sys.stdin.readline

cnt = 0
i = 1

for i in range(10):
    num = int(input())
    if num%2==1:
        cnt += 1
print(cnt)