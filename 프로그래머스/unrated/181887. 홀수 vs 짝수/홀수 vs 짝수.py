def solution(num_list):
    result0 = result1 = 0
    
    for i in range(0, len(num_list)):
        if(i % 2 == 0):
            result0 = result0 + num_list[i]
        else :
            result1 = result1 + num_list[i]
            
    if(result0 > result1):
        return result0
    
    return result1