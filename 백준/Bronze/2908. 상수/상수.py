a,b = map(str, input().split())

a = a[-1]+a[-2]+a[-3]
b = b[-1]+b[-2]+b[-3]

if(int(a) < int(b)):
    print(b)
else:
    print(a)