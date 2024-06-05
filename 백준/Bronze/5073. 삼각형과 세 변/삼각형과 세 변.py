while True:
    n1,n2,n3 = map(int, input().split())

    if(n1 == n2 == n3 == 0):
        break;
    
    array = []
    array.append(n1)
    array.append(n2)
    array.append(n3)

    array = sorted(array)

    if(array[0] + array[1] <= array[2]):
        print('Invalid')
    elif(n1 == n2 == n3):
        print('Equilateral')
    elif(n1 == n2 or n1 == n3 or n2 == n3):
        print('Isosceles')
    else:
        print('Scalene')