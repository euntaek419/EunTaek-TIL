def solution(n):
    a = []
    
    a.append(n)
    
    for i in range(0, 1001):
        
        if(n % 2 == 0):
            n = n / 2
        else:
            n = 3 * n + 1
        
        a.append(n)
        
        if(n == 1):
            return a