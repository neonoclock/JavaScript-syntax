import sys 
input = sys.stdin.readline

while True:
    N = int(input())
    if N < 25:
        print('Higher')
        continue
    if N > 25:
        print('Lower')
        continue
    if N == 25:
        print('Good')
        break