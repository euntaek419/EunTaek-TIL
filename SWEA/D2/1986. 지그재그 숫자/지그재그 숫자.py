T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    n = int(input())
    num = 0
    for i in range(1, n+1):
        if(i % 2 != 0):
            num = num + i
        else:
            num = num - i
    
    print("#{} {}".format(tc, num))