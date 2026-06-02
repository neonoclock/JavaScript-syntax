import sys
input = sys.stdin.readline

N=int(input())

while N<=100:
    if N>=90:
        print('A', end=' ')
    elif N>=80 and N<90:
        print('B', end=' ')
    elif N>=70 and N<80:
        print('C', end=' ')
    elif N>=60 and N<70:
        print('D', end=' ')
    else:
        print('F', end=' ')
    N+=1