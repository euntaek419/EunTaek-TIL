def solution(my_string):
    
    my_string = list(my_string)
    
    for i in range(0, len(my_string)):
        if(my_string[i].isupper() == False):
            my_string[i] = my_string[i].upper()
            
        elif(my_string[i].islower() == False):
            my_string[i] = my_string[i].lower()
    
    my_string = ''.join(map(str, my_string))
    
    return my_string