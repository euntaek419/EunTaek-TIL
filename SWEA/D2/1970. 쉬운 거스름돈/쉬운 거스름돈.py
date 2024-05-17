T = int(input())

for tc in range(1, T + 1):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    n = int(input())
    if(n / 50000 > 0):
        result[0] = n // 50000
        n = n % 50000
    
    if(n / 10000 > 0):
        result[1] = n // 10000
        n = n % 10000
    
    if(n / 5000 > 0):
        result[2] = n // 5000
        n = n % 5000
    
    if(n / 1000 > 0):
        result[3] = n // 1000
        n = n % 1000
    
    if(n / 500 > 0):
        result[4] = n // 500
        n = n % 500
    
    if(n / 100 > 0):
        result[5] = n // 100
        n = n % 100
    
    if(n / 50 > 0):
        result[6] = n // 50
        n = n % 50
    
    if(n / 10 > 0):
        result[7] = n // 10
        n = n % 10

    result = ' '.join(map(str, result))

    print("#{}".format(tc))
    print(result)