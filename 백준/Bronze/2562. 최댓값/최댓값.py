import sys
input = sys.stdin.readline

result = []

while True:
    try:
        A = int(input())
        result.append(A)
    except:
        break;

print(max(result), result.index(max(result))+1)