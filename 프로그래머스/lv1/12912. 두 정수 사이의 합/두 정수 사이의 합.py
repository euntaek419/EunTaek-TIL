def solution(a, b):
    count = 0
    if(a<=b):
        for i in range(a,b+1):
            count = count + i
        return count
    
    elif(a>=b):
        for i in range(b,a+1):
            count = count + i
        return count