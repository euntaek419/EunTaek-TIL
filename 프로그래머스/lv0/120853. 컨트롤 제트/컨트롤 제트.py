def solution(s):
    
    z_l = []
    result = 0
    
    z = 'Z'
    s = s.split()
    
    for i in range(0, len(s)):
        if(s[i] == z):
            s[i] = s[i-1]
            z_l.append(i)

    s = list(map(int, s))
    
    for j in range(0, len(s)):
        result = s[j] + result
        
    for k in range(0, len(z_l)):
        result = result - s[z_l[k]] *2
        
    return result