def solution(my_string, index_list):
    my_syring = list(my_string)
    result = []
    
    for i in range(0, len(index_list)):
        result.append(my_string[index_list[i]])
        
    return ''.join(result)