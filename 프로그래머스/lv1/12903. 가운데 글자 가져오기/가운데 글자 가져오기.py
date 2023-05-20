def solution(s):
    
    a = len(s) // 2
    
    b = list(s)
    
    c = []
    
    if( len(s) % 2 != 0):
        return b[a]
    else:
        c.append(b[a-1])
        c.append(b[a])
        return ''.join(c)
        