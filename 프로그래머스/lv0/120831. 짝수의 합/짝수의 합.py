def solution(n):
    a = 0
    for i in range(1,n+1):
        if(i % 2 == 0 ):
            a = a + i
    return a