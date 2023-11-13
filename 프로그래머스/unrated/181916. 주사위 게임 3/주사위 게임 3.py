from collections import Counter

def solution(a, b, c, d):
    if(a == b == c == d):
        return int(str(a)*4)
    
    if(a != b and a != c and a != d and b != c and b != d and c != d):
        return min(a,b,c,d)
    
    if(a == b == c):
        return (10 * a + d) * (10 * a + d)
    
    if(a == b == d):
        return (10 * a + c) * (10 * a + c)
    
    if(a == c == d):
        return (10 * a + b) * (10 * a + b)
    
    if(b == c == d):
        return (10 * b + a) * (10 * b + a)
        
    if(a == b):
        if(c == d):
            return (a + c) * abs(a - c)
        else:
            return c*d
        
    if(a == c):
        if(b == d):
            return (a + b) * abs(a - b)
        else:
            return b*d
        
    if(a == d):
        if(b == c):
            return (a + b) * abs(a - b)
        else:
            return b*c
        
    if(b == c):
        if(a == d):
            return (b + a) * abs(b - a)
        else:
            return a*d
        
    if(b == d):
        if(a == c):
            return (b + a) * abs(b - a)
        else:
            return a*c
        
    if(c == d):
        if(a == b):
            return (c + a) * abs(c - a)
        else:
            return a*b
    