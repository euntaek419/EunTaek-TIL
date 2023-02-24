def solution(n):
    for i in range(1, 1000000+1):
        if(n % i == 1):
            return i