def solution(arr, queries):
    
    for i in range(0, len(queries)): #0 1 2
        
        for j in range(queries[i][0],queries[i][1]+1): #0~1 / 1~2 / 2~3
            
            if(queries[i][0] <= j and j <= queries[i][1]):
                arr[j] += 1
            
    return arr