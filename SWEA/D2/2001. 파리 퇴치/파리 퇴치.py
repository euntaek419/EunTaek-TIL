T = int(input())

for tc in range(1, T + 1):
    n,m = map(int, input().split()) #n은 배열의 크기 / m은 파리채 크기
    matrix = []

    for i in range(0, n):
        data = list(map(int, input().split()))
        matrix.append(data)

    result = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for x in range(i, i+m):
                for y in range(j, j+m):
                    temp = temp + matrix[x][y]
            
            if(temp > result):
                result = temp
    
    print('#{} {}'.format(tc,result))