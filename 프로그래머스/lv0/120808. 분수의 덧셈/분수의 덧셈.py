from math import gcd #파이썬 최대공약수 내장함수 호출
#from math import lcm 파이썬 최소공배수 내장함수 호출 *파이썬 버전 3.9上 / 프로그래머스 파이썬 버전 3.8.5

def solution(num1, den1, num2, den2):
    den = den1 * den2 // gcd(den1, den2) #최소공배수(분모) *최대공약수 gcd(den1,den2)
    
    den_1 = int(den / den1) #최소공배수로 첫번째 분모와 나눔
    den_2 = int(den / den2) #최소공배수로 두번째 분모와 나눔
    
    num = (den_1*num1) + (den_2*num2) #분자에 나눈 값을 곱해줌
    
    num_gcd = gcd(num, den) #값이 약분될 경우를 대비한 최대공약수
    
    return int(num/num_gcd), int(den/num_gcd) #결과값