def solution(arr):
    result = []
    for i in range(0, len(arr)):
        if(arr[i] == 2):
            result.append(i)
    
    if(len(result) == 0):
        return [-1]
    else:
        return arr[result[0]:result[-1]+1]