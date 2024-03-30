a,b = map(int, input().split())

if(b - 45 < 0):
    if(a > 0 ):
        b = b - 45 + 60
        a = a - 1
        print(a, b)
    else:
        b = b - 45 + 60
        a = 23
        print(a, b)
else:
    print(a, b-45)