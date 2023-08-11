def solution(num_list):
    a = 1
    b = 0
    for i in range(0, len(num_list)):
        a = num_list[i] * a
    
    for j in range(0, len(num_list)):
        b = b + num_list[j]
        
    b = b * b
    
    if(a > b):
        return 0
    else:
        return 1