import sys
input = sys.stdin.readline

cnt = 0

while cnt < 3:
    N = int(input())

    if N % 2 == 1:
        continue

    print(N // 2)
    cnt += 1