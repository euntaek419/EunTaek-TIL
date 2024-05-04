def solution(n, m, section): #전체길이, 페인트 길이, 벗겨진 부분
    
    array = [True] * (n+1)
    count = 0
    
    for i in section:
        array[i] = False
        
    for i in range(0,len(array)):
        if(array[i] == False):
            count = count + 1
            array[i] = True
            for j in range(m):
                if i + j <= n:
                    array[i+j] = True
                
    return count