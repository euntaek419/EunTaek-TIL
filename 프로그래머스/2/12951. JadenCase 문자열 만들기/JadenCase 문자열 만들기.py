def solution(s):
    s = s.lower()
    
    s = list(s)
    
    s[0] = s[0].upper()
    
    for i in range(0, len(s)):
        if(s[i] == ' '):
            if(i < len(s)-1):
                s[i+1] = s[i+1].upper()
    
    return ''.join(s)