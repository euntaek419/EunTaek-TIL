import re
def solution(my_string):
    
    result = 0
    
    my_string = re.sub(r'[^0-9]', '', my_string)
    my_string = list(map(int, my_string))
    
    for i in my_string:
        result = i + result
        
    return result