def solution(n):
    
    a = 0
    n = str(n)
    n = list(n)
    
    for i in range (0, len(n)):
        a = a + int(n[i])
    
    return a