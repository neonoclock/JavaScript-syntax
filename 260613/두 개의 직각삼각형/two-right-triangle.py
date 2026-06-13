import sys
input = sys.stdin.readline

N = int(input())

for i in range(N, 0, -1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)