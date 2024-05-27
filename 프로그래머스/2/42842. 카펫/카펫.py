def solution(brown, yellow):
    
    t = brown + yellow
    
    result = []
    temp = len(result)
    
    for i in range(1, t+1):
        if(t % i == 0):
            result.append(i)
    
    if(len(result) % 2 != 0):
        return [result[len(result)//2], result[len(result)//2]]
    else:
        for i in range(0, len(result)):
            if((result[i]-2)*(result[temp-1]-2) == yellow):
                return [result[temp-1], result[i]]
            else:
                temp -= 1
            