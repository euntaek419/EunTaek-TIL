def solution(emergency):
    
    emsort = sorted(emergency, reverse=True)
    result = [0] * len(emsort)
    k = 1
    
    for i in range(0, len(emsort)):
        for j in range(0, len(emsort)):
            if(emsort[i] == emergency[j]):
                result[j] = k
                k = k+1
    
    return result