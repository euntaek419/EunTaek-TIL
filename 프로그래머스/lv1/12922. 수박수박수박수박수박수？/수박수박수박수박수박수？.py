def solution(n):
    
    a = []
    
    for i in range(1, n+1):
        if(i % 2 == 0):
            a.append('박')
        else:
            a.append('수')
    
    return ''.join(a) 