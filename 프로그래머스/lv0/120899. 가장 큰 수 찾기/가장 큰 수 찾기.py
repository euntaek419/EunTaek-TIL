def solution(array):
    
    result = []
    result.append(max(array))
    
    for i in range(0, len(array)):
        if(array[i] == max(array)):
            result.append(i)
    
    return result