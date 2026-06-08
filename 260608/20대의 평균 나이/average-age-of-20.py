import sys
input = sys.stdin.readline

age_sum = 0
cnt = 0

while True:
    N = int(input())

    if N < 20 or N >= 30:
        break

    age_sum += N
    cnt += 1

print(f"{age_sum / cnt:.2f}")