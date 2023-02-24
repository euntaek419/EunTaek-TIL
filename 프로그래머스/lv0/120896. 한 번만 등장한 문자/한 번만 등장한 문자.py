def solution(result):
    
    answer = ''
    
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if result.count(i) == 1:
            answer = answer + i
            
    return answer