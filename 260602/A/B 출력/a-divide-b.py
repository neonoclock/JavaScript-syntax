import sys
input = sys.stdin.readline

A, B = map(int, input().split())

integer_part = A // B
remainder = A % B

decimal_part = (remainder * 10**20) // B

print(f"{integer_part}.{decimal_part:020d}")