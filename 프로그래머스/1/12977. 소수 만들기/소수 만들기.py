from itertools import *

def solution(nums):
    
    #소수 목록 구하기
    count = [True] * 3000
    count[0] = count[1] = False
    
    for i in range(2, 3000):
        if count[i]:
            for j in range(i*i, 3000, i):
                count[j] = False
    
    #세 수를 합해서 소수인지 확인하기
    numList = list(combinations(nums, 3))
    array = 0
    
    for i in range(0, len(numList)):
        if(count[sum(numList[i])]):
            array += 1
    
    return array