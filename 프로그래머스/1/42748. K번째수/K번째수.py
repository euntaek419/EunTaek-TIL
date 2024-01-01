def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command
        result = sorted(array[i-1:j])[k-1]
        answer.append(result)
    
    return answer