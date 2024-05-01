T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    num = list(map(int, input().split()))
    num = sorted(num)
    n = 0
    for i in range(1, 9):
        n = n + num[i]
    n = round(n/8)
    
    print("#{} {}".format(tc, n))