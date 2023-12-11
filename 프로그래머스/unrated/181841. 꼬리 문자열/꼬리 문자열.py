def solution(str_list, ex):
    result = str_list.copy()
    
    for i in range(0, len(str_list)):
        if(ex in str_list[i]):
            result.remove(str_list[i])
    
    return ''.join(result)