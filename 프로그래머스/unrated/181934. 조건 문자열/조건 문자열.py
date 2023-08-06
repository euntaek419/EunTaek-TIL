def solution(ineq, eq, n, m):
    if(ineq == '>'): # '>' 일때
        if(eq == '='): # '>','=' 일때
            if(n >= m): # 일치 확인
                return 1
            else:
                return 0
        else: #'> '!'
            if( n < m):
                return 0
            else:
                return 1
            
            
    else: # '<' 일때
        if(eq == '='):# '<','=' 일때
            if(n <= m): # 일치 확인
                return 1
            else:
                return 0
        else:
            if(n > m):
                return 0
            else:
                return 1
            