def solution(my_string):
    result = [0] * 52
    
    for i in my_string:
        if(i.isupper()):
            result[ord(i)-65] += 1 #25번 까지 인덱스 계산 
        else:
            result[ord(i)-71] += 1 #26번 부터 인덱스 계산 97 - 26 = 71 대문자의 인덱스를 제외하고 이후의 인덱스
    
    return result