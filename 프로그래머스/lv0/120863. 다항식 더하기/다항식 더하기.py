def solution(polynomial):
    
    polynomial = polynomial.split()
    
    result = [] # 사칙연산을 제외한 x와 숫자 
    x_temp = [] # x가 모일 공간 
    n_temp = [] # 정수가 모일 공간 
    mark = [] # +-*/ 마크가 모일 공간 
    x = n = c1 = c2 = 0
    answer = []
    
    #사칙 연산
    for i in range(0, len(polynomial)):
        if(i % 2 == 0):
            result.append(polynomial[i]) #마크를 제외하고 보냄
        else:
            mark.append(polynomial[i]) #마크가 모일 공간으로 보냄
    
    
    for j in range(0, len(result)):
        if(result[j].find('x') > -1): #x표시가 있을 경우
            if(result[j] == 'x'): # x는 1x로 변경 후
                result[j] = '1x'
            
            x_temp.append(result[j]) # x_temp에 x들 저장
        
        if(str.isdigit(result[j]) == True): # 정수일경우
            n_temp.append(result[j]) # n_temp에 정수들 저장
        
    
    for k in range(0, len(x_temp)): 
        x_temp[k] = x_temp[k].replace("x", "") # x를 떼고
        x = x + int(x_temp[k]) # x를 더해서 저장
    
    if(x == 1):
        x = "x"
        answer.append(x)
        c1 = 1
    
    elif(x > 0):
        x = str(x) + "x" # x가 0보다 크면 x를 다시 붙임
        answer.append(x)
        c1 = 1
    
        
    for l in range(0, len(n_temp)):
        n = n + int(n_temp[l])
    
    if(n > 0):
        answer.append(str(n))
        c2 = 1
        
    if(c1 == 1 and c2 ==1):
        answer.insert(1, "+")
    
    answer = ' '.join(answer)
    
    return answer