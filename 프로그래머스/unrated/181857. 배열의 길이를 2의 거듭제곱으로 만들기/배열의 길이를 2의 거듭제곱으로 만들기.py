def solution(arr):
    
    if(len(arr) == 1):
        return arr
    
    i = 2
    
    while i < 1000:
        if(len(arr) <= i):
            break;
        else:
            i = i*2
    
    for j in range(0, i):
        if(i > len(arr)):
            arr.append(0)
            
    return arr