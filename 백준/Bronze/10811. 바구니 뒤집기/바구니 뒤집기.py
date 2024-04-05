import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = list(range(1, N+1))

for i in range(M):
    a, b = map(int, input().split())
    result[a-1:b] = reversed(result[a-1:b])

print(' '.join(map(str, result)))