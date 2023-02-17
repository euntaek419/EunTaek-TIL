from math import gcd #파이썬 최대공약수 내장함수 호출 
def solution(denum1, num1, denum2, num2): 
    m = num1 * num2 // gcd(num1, num2) #최소공배수(분모)  *최대공약수 gcd(num1, num2)
    
    sx1 = int(m / num1)
    sx2 = int(m / num2)
    
    s = (sx1*denum1) + (sx2*denum2)

    ml = gcd(s, m)

    return int(s/ml),int(m/ml)