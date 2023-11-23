def solution(my_string, is_prefix):
    result = []

    for i in range(1,len(my_string)+1):
        result.append(my_string[:i])
    
    if(is_prefix in result):
        return 1
    else:
        return 0
    
