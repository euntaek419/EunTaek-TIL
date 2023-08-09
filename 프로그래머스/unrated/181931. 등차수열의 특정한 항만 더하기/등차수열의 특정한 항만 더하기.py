def solution(a, d, included):
    
    result = 0
    num = 0
    
    if(included[0] == True):
        result = result + a
    
    for i in range(0, len(included)):
        
        num = i*d
        if(i >= 1 and included[i] == True):
            result = result + a + num
    
    return result