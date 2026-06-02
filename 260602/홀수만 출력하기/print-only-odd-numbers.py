import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    i = int(input())
    if i%3==0 and i%2==1:
        print(i)