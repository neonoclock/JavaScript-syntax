import sys
input = sys.stdin.readline

while True:
    A, B, C = input().split()
    A, B = int(A), int(B)
    print(A*B)
    if C == 'C':
        break