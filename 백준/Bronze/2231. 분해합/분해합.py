n = int(input())

result = 0



for i in range(0,n): #1부터 입력받은 수까지 반복

    num = i
    sum = 0

    for j in range(0, len(str(i))): #num을 i의 길이수만큼 나누기

        sum = sum + num % 10 #num 의 나머지를 저장
        num = num // 10 #num을 나눔

    if (i + sum == n):
        result = i
        print(i)
        exit(0)

print(0)
