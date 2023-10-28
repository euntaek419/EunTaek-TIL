def solution(rny_string):
    answer = []
    rny_string = list(rny_string)
    
    for i in range(0, len(rny_string)):
        if(rny_string[i] != 'm'):
            answer.append(rny_string[i])
        else:
            answer.append('r')
            answer.append('n')
    
    answer = ''.join(answer)
    return answer