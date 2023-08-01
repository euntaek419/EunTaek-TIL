def solution(my_string, overwrite_string, s):
    my_string = list(my_string)
    overwrite_string = list(overwrite_string)
    
    for i in range(0, len(overwrite_string)):
        my_string[s+i] = overwrite_string[i]
    
    return ''.join(my_string)
            