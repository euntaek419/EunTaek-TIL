while True:
    data = list(map(int, input().split()))

    data = sorted(data)

    if(sum(data) == 0):
        break;
    
    if( (data[0]*data[0] + data[1]*data[1]) == data[2]*data[2]):
        print('right')
    else:
        print('wrong')