def solution(n):
    result = []
    
    for i in range(0, n):
        result.append([0]*n)
    
    count = 1
    up, down, left, right = 0, n-1, 0, n-1
    
    while count <= n * n:
        #좌측 -> 우쪽
        for i in range(left, right + 1): #0부터 n 까지
            result[up][i] = count #0의 0~n까지 카운터
            count += 1
        up += 1
        
        #위 -> 아래
        for i in range(up, down + 1): #0부터 n 까지
            result[i][right] = count #0~n의 n-1 까지 카운터
            count += 1
        right -= 1 #다 넣었으면 우측에서 한 칸 마이너스
        
        #우측 -> 좌측
        for i in range(right, left - 1, -1): #n-1 부터 -1까지
            result[down][i] = count #n-1부터 n~-1까지 카운터
            count += 1
        down -= 1 #다 넣었으면 아래에서 한 칸 마이너스
        
        #아래 -> 위
        for i in range(down, up - 1, -1):
            result[i][left] = count 
            count += 1
        left += 1
        
    return result