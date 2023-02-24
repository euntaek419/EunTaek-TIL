def solution(s1, s2):
    
    result = 0
    
    for i in range(0, len(s1)):
        if(s1[i] in s2):
            result = result +1
            
    return result
            