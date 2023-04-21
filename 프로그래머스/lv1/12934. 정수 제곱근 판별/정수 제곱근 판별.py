import math;

def solution(n):
    
    n = math.sqrt(n) + 1;
    a = n * n;
    
    if( math.ceil(a) > a):
        return -1;
    else:
        return a;