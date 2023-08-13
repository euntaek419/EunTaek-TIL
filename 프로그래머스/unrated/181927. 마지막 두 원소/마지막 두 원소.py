def solution(num_list):
    a = len(num_list) -1
    
    if(num_list[a] > num_list[a-1]):
        num_list.append(num_list[a] - num_list[a-1])
    else:
        num_list.append(num_list[a] * 2)
    
    return num_list