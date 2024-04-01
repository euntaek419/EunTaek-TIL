import sys
input = sys.stdin.readline #문자열 입력

while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
    except:
        break;