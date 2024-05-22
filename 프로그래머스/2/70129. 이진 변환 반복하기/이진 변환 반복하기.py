def solution(s):
    
    count = 0 #회차
    zeroCount = 0 #제거할 0의 개수
    
    while s != '1':
        count += 1
        s = list(s)
        for i in range(0, len(s)):
            if(s[i] == '0'):
                zeroCount += 1
                s[i] = ''
        
        s = str(bin(len(list(''.join(s))))[2:])
    
    return [count, zeroCount]