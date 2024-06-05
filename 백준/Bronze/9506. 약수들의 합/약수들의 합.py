n = int(input())

while n != -1:
    array = []
    for i in range(1, n):
        if(n%i == 0):
            array.append(i)
    
    if(sum(array) == n):
        print(n, '=', ' + '.join(map(str, array)))
        n = int(input())
    else:
        print(n, 'is NOT perfect.')
        n = int(input())