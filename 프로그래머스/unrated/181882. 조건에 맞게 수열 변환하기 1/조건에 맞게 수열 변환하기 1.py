def solution(arr):
    for i in range(0, len(arr)):
        if(arr[i] >= 50 and arr[i] % 2 == 0):
            arr[i] = arr[i] / 2
        elif(arr[i] < 50 and arr[i] % 2 != 0):
            arr[i] = arr[i] * 2
        
    return arr