def solution(my_string, n):
    new_string = []
    my_string = list(my_string)
    for i in range(0,len(my_string)):
        new_string.append(my_string[i] * n)
    return "".join(new_string)