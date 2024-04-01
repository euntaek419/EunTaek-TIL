import sys
input = sys.stdin.readline #문자열 입력

A = int(input())

zero = 1

for i in range(A-1, -1, -1):
    print( " "*i + '*'*zero)
    zero += 1