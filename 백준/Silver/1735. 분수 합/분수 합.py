def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)

n1,a = map(int, input().split())
n2,b = map(int, input().split())    

ab = lcm(a,b)

a = (ab // a) * n1
b = (ab // b) * n2

result = gcd(a+b, ab)

if(result == 1):
    print(a+b, ab)
else:
    print( (a+b)// result, ab//result)