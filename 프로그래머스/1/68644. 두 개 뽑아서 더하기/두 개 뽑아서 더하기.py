from itertools import *

def solution(numbers):
    result = list(combinations(numbers, 2))
    answer = []
    
    for i in range(0, len(result)):
        answer.append(sum(result[i]))
    
    result = set(answer)
    
    return sorted(list(result))