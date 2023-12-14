def solution(arr):
    
    result = []
    
    for i in range(0, len(arr)):
        if(arr[i:i+1] != arr[i+1:i+2]):
            result.append(arr[i])
    
    return result