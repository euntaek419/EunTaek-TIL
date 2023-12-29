def solution(s):
    s = list(s)
    
    num = 0
    
    for i in range(0, len(s)):
        if(s[i] == " "):
            num = 0
            print(i)
        else:
            if(num % 2 == 0):
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
            num += 1
            
    return ''.join(s)