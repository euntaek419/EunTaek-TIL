def solution(arr):
    n = 1 # 모든 곱셈
    for i in arr: #모든 곱셈 구하기
        n = n * i
    
    arr = sorted(arr) # arr정렬
    
    
    for i in range(2, n): #곱의 약수 구하기 2 3 4 5 6 7
        if(n % i == 0 and arr[-1] <= i): #정렬된 마지막 숫자랑 크거나 같아야함
            l = len(arr) # arr길이
            for j in arr: #arr의 길이만큼 반복 2 6 8 14
                if(i % j == 0 ):
                    l -= 1
                    if(l == 0):
                        return i
                else:
                    l = len(arr)
                    continue
                    
    
    return n