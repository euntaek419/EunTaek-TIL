n = int(input())
n1, n2 = map(int, input().split())

result = [n1,n2,n1,n2]

while n-1 > 0:
    n3, n4 = map(int, input().split())
    if(result[0] > n3):
        result[0] = n3
    if(result[1] > n4):
        result[1] = n4
    if(result[2] < n3):
        result[2] = n3
    if(result[3] < n4):
        result[3] = n4
    
    n -= 1

print( (result[2]-result[0]) * (result[3] - result[1]) )