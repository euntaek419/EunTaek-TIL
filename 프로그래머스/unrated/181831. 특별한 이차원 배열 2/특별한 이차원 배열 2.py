def solution(arr):
    a = len(arr)
    b = len(arr[0])
    
    for i in range(0, a):
        for j in range(0, b):
            if(arr[i][j] != arr[j][i]):
                return 0
    
    return 1
                