import sys
input = sys.stdin.readline #문자열 입력

a,b = map(int, input().split())

while (a != 0 and b != 0):
    print(a+b)
    a,b = map(int, input().split())