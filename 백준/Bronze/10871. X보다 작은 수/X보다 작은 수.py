import sys
input = sys.stdin.readline

a,b = map(int, input().split())
data = list(map(int, input().split()))
result = []

for i in range(0,a):
    if(data[i] < b):
        result.append(str(data[i]))

result = ' '.join(result)

print(result)