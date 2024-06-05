n1, n2 = map(int, input().split())

while n1 != n2 != 0:
    if(n1 % n2 == 0):
        print('multiple')
        n1, n2 = map(int, input().split())
    elif(n2 % n1 == 0):
        print('factor')
        n1, n2 = map(int, input().split())
    else:
        print('neither')
        n1, n2 = map(int, input().split())