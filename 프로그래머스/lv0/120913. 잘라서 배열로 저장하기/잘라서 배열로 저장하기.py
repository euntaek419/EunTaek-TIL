def solution(my_str, n):
    
    my_str = list(my_str)
    
    result = []
    temp1 = []
      
    for i in range(0, len(my_str)):
        temp1.append(my_str[i])
        
        
        if(len(temp1) % n == 0):
            result.append(str(''.join(map(str, temp1))))
            temp1 = []
        
        elif(i+1 == len(my_str)):
            result.append(str(''.join(map(str, temp1))))
            
    return result