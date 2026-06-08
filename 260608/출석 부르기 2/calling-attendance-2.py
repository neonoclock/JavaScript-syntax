import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 1:
        print('John')
        continue
    if N == 2:
        print('Tom')
        continue
    if N == 3:
        print('Paul')
        continue 
    if N == 4:
        print('Sam')
        continue
    else:
        print('Vacancy')
        break