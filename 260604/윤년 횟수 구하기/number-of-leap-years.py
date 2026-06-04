import sys
input = sys.stdin.readline

N = int(input())

cnt_yun = 0

for i in range(1, N+1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        cnt_yun += 1
print(cnt_yun)
        