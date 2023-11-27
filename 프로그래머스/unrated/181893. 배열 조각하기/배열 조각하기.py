def solution(arr, query):
    
    num = 0
    
    for i in query:
        if(num % 2 == 0):
            arr = arr[:i+1]
        else:
            arr = arr[i:]
        
        num += 1
    
    return arr