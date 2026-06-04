import sys
input = sys.stdin.readline

n = int(input())

cnt_class = 0
cnt_road = 0
cnt_toilet = 0

for i in range(1, n + 1):
    if i % 12 == 0:
        cnt_toilet += 1
    elif i % 3 == 0:
        cnt_road += 1
    elif i % 2 == 0:
        cnt_class += 1
print(cnt_class, cnt_road, cnt_toilet, end=' ')