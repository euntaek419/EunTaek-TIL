def solution(my_string):
    result = []

    for i in range(len(my_string)-1,-1, -1):
        result.append(my_string[i:])
    
    return sorted(result)