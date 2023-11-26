def solution(arr, idx):
    result = []
    
    for i in range(0,len(arr)):
        if(i >= idx and arr[i] != 0):
            result.append(i)

    if(len(result) == 0):
        return -1
    else:
        return min(result)