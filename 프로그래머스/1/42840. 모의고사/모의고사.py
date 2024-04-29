def solution(answers):
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    resultA = 0
    resultB = 0
    resultC = 0
    
    for i in range(0, len(answers)):
        if(answers[i] == a[i]):
            resultA = resultA + 1
        
        if(answers[i] == b[i]):
            resultB = resultB + 1
        
        if(answers[i] == c[i]):
            resultC = resultC + 1
    
    if(resultA > resultB and resultA > resultC):
        return [1]
    elif(resultB > resultA and resultB > resultC):
        return [2]
    elif(resultC > resultA and resultC > resultB):
        return [3]
    elif(resultA == resultB and resultA > resultC):
        return [1,2]
    elif(resultA == resultC and resultA > resultB):
        return [1,3]
    elif(resultB == resultC and resultB > resultA):
        return [2,3]
    else:
        return [1,2,3]