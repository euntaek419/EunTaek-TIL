def solution(numbers, n):
    
    a = 0
    
    for i in range(0, len(numbers)):
        if(a <= n):
            a = numbers[i] + a
            if(a > n):
                return a
        else:
            return a