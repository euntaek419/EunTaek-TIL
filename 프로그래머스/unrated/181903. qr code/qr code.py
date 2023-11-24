def solution(q, r, code):
    
    code = list(code)
    result = []
    
    for i in range(0, len(code)):
        if(i % q == r):
            result.append(code[i])
    
    return ''.join(result)