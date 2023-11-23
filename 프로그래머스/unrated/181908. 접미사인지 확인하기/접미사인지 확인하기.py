def solution(my_string, is_suffix):
    result = []

    for i in range(len(my_string)-1,-1, -1):
        result.append(my_string[i:])
    
    if(is_suffix in result):
        return 1
    else:
        return 0