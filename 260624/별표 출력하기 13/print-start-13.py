import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    if i % 2 == 0:
        print("* " * (i // 2))
    else:
        print("* " * (N - i // 2))

for i in range(N, 0, -1):
    if i % 2 == 0:
        print("* " * (i // 2))
    else:
        print("* " * (N - i // 2))