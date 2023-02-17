def solution(n, k): #n = 인분, k = 음료
    f = n // 10 # f는 양꼬치
    return n * 12000 + k * 2000 - f * 2000