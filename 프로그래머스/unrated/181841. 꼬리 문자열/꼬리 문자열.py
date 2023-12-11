def solution(str_list, ex):
    for i in range(0, len(str_list)):
        if(ex in str_list[i]):
            str_list[i] = str_list[i] - ex
    
    return str_list    