def solution(arr, n):
    
    if(len(arr) % 2 != 0):
        for i in range(0, len(arr)):
            if(i % 2 == 0):
                arr[i] += n
    else:
        for j in range(0, len(arr)):
            if(j % 2 != 0):
                arr[j] += n
                        
    return arr