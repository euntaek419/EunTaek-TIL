T = int(input())
for tc in range(1, T + 1):
    a,b = map(int, input().split())
    dataA = list(map(int, input().split()))
    dataB = list(map(int, input().split()))

    result = 0

    if(a > b):
        for i in range(0, a-b+1):
            temp = 0
            for j in range(0, b):
                temp = temp + dataA[i+j] * dataB[j]
            if(temp > result):
                result = temp
    elif(a < b):
        for i in range(0, b-a+1):
            temp = 0
            for j in range(0, a):
                temp = temp + dataA[j] * dataB[i+j]
            if(temp > result):
                result = temp
    else:
        for i in range(a):
            result = result + dataA[i] + dataB[i]

    print('#{} {}'.format(tc, result))