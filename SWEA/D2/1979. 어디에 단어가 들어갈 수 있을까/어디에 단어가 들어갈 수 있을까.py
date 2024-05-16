T = int(input())

for tc in range(1, T + 1):
    n,k = map(int, input().split()) #최대단어길이 k
    
    #n*n의 길이의 2차원 배열
    #array = [[0 for i in range(n)] for i in range(n)] #0으로 채우는 코드

    array = []

    for i in range(n):
        r = list(map(int, input().split()))

        array.append(r)
    
    count = 0

    #[i]번째 인덱스부터 n번째 인덱스까지 검사
    #[i][j]번째 인덱스부터 [i][n] 번째 인덱스까지 검사하는데
    #[i][j]번째 인덱스부터 [i][j+k] 번째 인덱스까지 0인지 조사
    for i in range(n):
        temp = 0
        
        for j in range(n):
            if(array[i][j] == 1):
                temp += 1
            if( array[i][j] == 0 or j == n-1):
                if(temp == k):
                    count += 1
                temp = 0
        
        for j in range(n):
            if(array[j][i] == 1):
                temp += 1
            if(array[j][i] == 0 or j == n-1):
                if (temp == k):
                    count += 1
                temp = 0
    
    print('#{} {}'.format(tc, count))