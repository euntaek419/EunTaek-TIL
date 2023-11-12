def solution(my_string, n):
    my_string = list(reversed(my_string))
    
    my_string = my_string[:n]
    
    my_string = reversed(my_string)
    
    my_string = ''.join(my_string)
    
    return my_string