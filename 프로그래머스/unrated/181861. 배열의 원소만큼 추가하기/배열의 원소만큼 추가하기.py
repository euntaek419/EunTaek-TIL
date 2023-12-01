def solution(arr):
    result = []
    for i in range(0,len(arr)):
        for j in range(0,arr[i]):
            result.append(arr[i])
    return result