def solution(t, p):
    result = 0
    for i in range(0, len(t)):
        if(len(t[i:i+len(p)]) == len(p) and t[i:i+len(p)] <= p):
            result += 1
    
    return result