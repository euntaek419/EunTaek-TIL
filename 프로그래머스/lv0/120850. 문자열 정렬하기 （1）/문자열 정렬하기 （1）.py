import re
def solution(my_string):
    my_string = re.sub(r'[^0-9]', '', my_string)
    my_string = list(map(int, my_string))
    my_string.sort()
    return my_string