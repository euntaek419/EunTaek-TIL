def solution(arr, query):
    
    for i in query:
        if(i % 2 == 0):
            arr = arr[:i+1]
        else:
            arr = arr[i:]
    
    return arr