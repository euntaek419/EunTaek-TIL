def solution(my_string, num1, num2):
    
    my_string = list(my_string)
    
    a = my_string[num1]
    b = my_string[num2]
    
    my_string[num1] = b
    my_string[num2] = a
    
    my_string=''.join(map(str, my_string))
    
    return my_string