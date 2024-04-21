T = int(input())
for i in range(T):
    result = ['0', '0', '0', '0']

    money = int(input())
    if(money // 25 >= 1):
        result[0] = str(money // 25)
    money = money % 25

    if(money // 10 >= 1):
        result[1] = str(money // 10)
    money = money % 10

    if(money // 5 >= 1):
        result[2] = str(money // 5)
    money = money % 5

    if(money // 1 >= 1):
        result[3] = str(money // 1)

    print(' '.join(result))