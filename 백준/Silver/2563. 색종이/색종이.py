arr = [[0]*102 for _ in range(102)]

T = int(input())
for i in range(T):
    sj, si = map(int, input().split())
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = 1
    
    result = 0

    for i in arr:
        result = result + sum(i)

print(result)