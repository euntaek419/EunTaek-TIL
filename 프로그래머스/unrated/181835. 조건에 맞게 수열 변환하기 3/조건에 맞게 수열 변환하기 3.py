def solution(arr, k):
    
    if(k % 2 == 0):
        for i in range(0, len(arr)):
            arr[i] = arr[i] + k
    
    else:
        for j in range(0, len(arr)):
            arr[j] = arr[j] * k
        
    return arr