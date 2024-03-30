t,m = map(int, input().split())
p = int(input())

if(m+p // 60 > 0):
    t = t+(m+p) //60
    m = (m+p)%60

    if(t > 23 ):
        t = t - 24
        print(t, m)
    else:
        print(t, m)
else:
    print(t, m+p)