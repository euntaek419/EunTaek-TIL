from collections import Counter

def solution(numbers):
    c = Counter(numbers) #세기 함수
    order = c.most_common() #최빈값 구하기
    
    maximum = order[0][1] #최빈값 maximum에 저장
    modes = [] #배열만들고
    
    for num in order: 
        if num[1] == maximum: #최빈값과 센 값이 같으면
            modes.append(num[0]) #modes에 추가
    
            
    if(len(modes) >= 2): #modes의 갯수가 2개 이상이면
        modes = -1 #-1
    else: #아니면
        modes = int(str(modes)[1:-1]) #문자열로 변경하여 list 해체 후, 다시 정수로 변경
    
    return modes