T = int(input())

rank = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

for tc in range(1, T + 1): #테스트 케이스
    number = []
    n,k = map(int, input().split())
    same = int(n/10) # 스코어를 각각 same 명에게 줘야함.
    
    for i in range(0, n):
        n1,n2,n3 = map(int, input().split())
        number.append( n1*35 + n2*45 + n3*20 )
    
    tempNum = number # 정렬 안됨
    number = sorted(number) # 정렬됨

    count = 0

    for D0 in range(0, same):
        number[count] = (number[count], 'D0')
        count += 1

    for CM in range(0, same):
        number[count] = (number[count], 'C-')
        count += 1
    
    for C0 in range(0, same):
        number[count] = (number[count], 'C0')
        count += 1
    
    for CP in range(0, same):
        number[count] = (number[count], 'C+')
        count += 1

    for BM in range(0, same):
        number[count] = (number[count], 'B-')
        count += 1

    for B0 in range(0, same):
        number[count] = (number[count], 'B0')
        count += 1

    for BP in range(0, same):
        number[count] = (number[count], 'B+')
        count += 1

    for AM in range(0, same):
        number[count] = (number[count], 'A-')
        count += 1

    for A0 in range(0, same):
        number[count] = (number[count], 'A0')
        count += 1

    for AP in range(0, same):
        number[count] = (number[count], 'A+')
        count += 1

    for last in range(0, len(number)):
        if(tempNum[k-1] == number[last][0]):
            print("#{} {}".format(tc, number[last][1]))