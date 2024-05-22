def solution(n):
    
    count = 1
    
    for i in range(1, n//2+1):
        t = 0
        while t < n:
            t += i
            i += 1
        if(t == n):
            count += 1

    return count