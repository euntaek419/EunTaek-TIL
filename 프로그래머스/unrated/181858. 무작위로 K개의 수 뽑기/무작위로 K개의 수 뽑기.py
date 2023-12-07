def solution(arr, k):
    
    result = []
    
    for i in range(0,len(arr)):
        if(arr[i] not in result and len(result) < k):
            result.append(arr[i])
        
    while (len(result) < k):
        result.append(-1)
    
    return result