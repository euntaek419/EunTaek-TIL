def solution(arr):
    
    result = arr.copy()
    
    for test in range(0, 11):
        
        for i in range(0,len(arr)):
            if(arr[i] > 49 and arr[i] % 2 == 0):
                arr[i] = arr[i] // 2
            elif(arr[i] < 50 and arr[i] % 2 != 0):
                arr[i] = arr[i] * 2 + 1
        
        if(result == arr):
            return test
        else:
            result = arr.copy()
        
        