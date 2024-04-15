def solution(s):
    s = s.split()
    s = list(map(int, s))
    
    result = []
    result.append(str(min(s)))
    result.append(str(max(s)))
    
    return ' '.join(result)
    