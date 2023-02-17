def solution(num_list):
    
    a = b = 0

    for i in num_list:
        if(i % 2 == 0):
            a = a+1
        elif(i % 2 != 0):
            b = b+1
    
    result = []
    result.append(a)
    result.append(b)
    
    return result