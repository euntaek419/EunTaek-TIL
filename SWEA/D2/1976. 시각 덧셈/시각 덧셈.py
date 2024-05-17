T = int(input())

for tc in range(1, T + 1):
    t1, m1, t2, m2 = map(int, input().split())

    t = t1 + t2
    m = m1 + m2

    if(m1 + m2 > 59):
        m -= 60
        t += 1
    
    if( t > 12 ):
        t -= 12
    
    print('#{} {} {}'.format(tc, t, m))