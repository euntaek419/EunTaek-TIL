# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 한다.
# 세번째에 올 수 있는 정수의 '갯수'를 리턴

def solution(sides):
    
    m_side = sides[0] + sides[1] -1 # 가장 큰 사이드의 길이
    
    a = max(sides) - (max(sides)-(min(sides))) 
    
    b = m_side - max(sides) #나머지 한 변이 가장 긴 변인 경우
    
    return a+b