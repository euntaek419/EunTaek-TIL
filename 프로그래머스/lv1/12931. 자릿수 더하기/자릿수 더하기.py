def solution(n):
    
    result = 0
    
    n = list(str(n))
    
    n = list(map(int, n))
    
    for i in range(0, len(n)):
        result = result + n[i]
    
    return result