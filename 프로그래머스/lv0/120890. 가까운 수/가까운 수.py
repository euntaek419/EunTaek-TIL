def solution(array, n):
    
    array.append(n)
    array = sorted(array)
    
    A = B = result = 0
    
    if(max(array) == n):
        result = array[len(array)-2]
        return result
        
    elif(min(array) == n):
        result = array[0]
        return result
    
    else:
        for i in range(0, len(array)):
        
            if(array[i] == n):
                A = n - array[i -1]
                B = array[i+1] - n
            
                if(B-A >= 0):
                    return array[i-1]
                    
                elif(B-A < 0):
                    return array[i+1]