import sys
input = sys.stdin.readline

N,M = map(int, input().split()) #바구니 N개 / M번 실행
B = []

for i in range(0, N+1):
    B.append(i)

for i in range(M):
    a,b = map(int, input().split())
    B[a], B[b] = B[b], B[a]

B.pop(0)

print(' '.join(map(str, B)))