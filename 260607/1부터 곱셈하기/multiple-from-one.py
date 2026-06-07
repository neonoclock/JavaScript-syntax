import sys
input = sys.stdin.readline

N = int(input())

val = 1

for i in range(1, 11):
    val *= i

    if val >= N:
        print(i)
        break