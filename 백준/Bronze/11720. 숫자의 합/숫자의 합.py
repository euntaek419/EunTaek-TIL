N = int(input())
M = input()
M = list(M)
result = 0

for i in range(0, N):
    result = result + int(M[i])

print(result)