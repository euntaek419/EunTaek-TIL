def solution(arr, flag):
    
    result = []
    
    for i in range(0,len(flag)):
        if(flag[i] == True):
            for j in range(0, arr[i]*2):
                result.append(arr[i])
        else:
            for k in range(0, arr[i]):
                result.pop()
    return result