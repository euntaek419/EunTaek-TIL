import sys
input = sys.stdin.readline

result = []

for i in range(0, 10):
    a = int(input())
    result.append(a%42)

print(len(set(result)))