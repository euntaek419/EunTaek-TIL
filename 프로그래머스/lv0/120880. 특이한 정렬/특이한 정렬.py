def solution(numlist, n):
    answer = sorted(numlist, key = lambda x : (abs(x-n), -x))
    
    #sorted(numlist, key = lambda x : ( , ))
    
    #abs() = 절대값 변환
    
    #sorted(정렬할 데이터, key 파라미터)
    #(lambda x,y: x + y)(10, 20)
    
    #공부를 더 해볼 것..!!
    
    return answer