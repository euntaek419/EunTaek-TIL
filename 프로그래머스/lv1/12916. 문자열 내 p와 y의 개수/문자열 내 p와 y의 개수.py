def solution(s):
    s = s.lower();
    a = s.count("p");
    b = s.count('y');
    
    if(a == b):
        return True;
    else:
        return False;
        