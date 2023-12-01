def solution(num_str):
    result = 0
    num_str = list(num_str)
    
    for i in num_str:
        result = result   + int(i)
    
    return result