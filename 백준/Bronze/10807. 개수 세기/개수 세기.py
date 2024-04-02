import sys
input = sys.stdin.readline

T = int(input())
data = list(map(int, input().split()))
need = int(input())
result = 0

for i in range(0, T):
    if(data[i] == need):
        result = result + 1

print(result)