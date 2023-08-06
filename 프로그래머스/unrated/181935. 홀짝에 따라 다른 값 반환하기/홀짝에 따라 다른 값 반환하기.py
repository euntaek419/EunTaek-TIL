def solution(n):
    result = 0
    
    if(n % 2 == 0):
        for i in range(0, n+1):
            if( i % 2 == 0):
                result = result + i * i
    else:
        for j in range(0, n+1):
            if( j % 2 != 0):
                result = result + j
    
    return result