T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    array = []
    empArray = [[0]*m] * n
    for i in range(0, n):
        temp = list(map(int, input().split()))
        array.append(temp)
    
    bigData = 0

    for i in range(0, n):
        for j in range(0, m):
            value = array[i][j]

            if i > 0:
                value += array[i-1][j]
            
            if i < n-1:
                value += array[i+1][j]
            
            if j > 0:
                value += array[i][j-1]

            if j < m-1:
                value += array[i][j+1]

            empArray[i][j] = value

            if(value > bigData):
                bigData = value
    
    print("#{} {}".format(tc, bigData))