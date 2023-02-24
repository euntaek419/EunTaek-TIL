def solution(a, b, c):
    
    result = []
    num = 0
    
    for i in range(a, b+1):
        result.append(i)
    
    
    result = int(''.join(map(str, result)))
    result = list(map(int,str(result)))
    
    for i in range(0, len(result)):
        if(result[i] == c):
            num = num +1
    
    return num