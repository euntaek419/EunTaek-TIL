T = int(input())

for i in range(T):
    ox = list(input())
    total = 0
    num = 0
    for i in range(0, len(ox)):
        if(ox[i] == 'O'):
            num = num + 1
            total = total + num
        else:
            num = 0
            total = num + total
    
    print(total)