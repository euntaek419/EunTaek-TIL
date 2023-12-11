def solution(arr, delete_list):
    result = arr.copy()
    
    for i in arr:
        for j in delete_list:
            if(i == j):
                result.remove(i)
    
    return result
                
                
        