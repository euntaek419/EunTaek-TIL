def solution(s):
    s = list(s)
    
    for i in range(0, len(s)):
        if(i % 2 == 0):
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()

    return ''.join(s)