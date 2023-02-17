from math import gcd
def solution(n):
    return ((n * 6) // gcd(n, 6) // 6) #사람과 피자 조각의 최소공배수

# n = 사람
# r = 몇판인지 (피자는 반드시 6조각)