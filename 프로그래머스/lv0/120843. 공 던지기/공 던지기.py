def solution(numbers, k):
    k = k*2
    result = 0
    if(k > len(numbers)):
        rm = k % len(numbers)
        result = numbers[rm-2]
    else:
        result = numbers[k-2]
    
    return result