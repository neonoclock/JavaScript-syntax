import sys
input = sys.stdin.readline

N = int(input())

for i in range(2):
    for j in range(N):
        for h in range(N):
            print('*', end='')
        print()
    print()
