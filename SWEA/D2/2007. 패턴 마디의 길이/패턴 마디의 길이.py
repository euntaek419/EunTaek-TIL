T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    h = list(input())
    
    i = 1
    while i < 30:
        if(h[0:i] == h[i:i+i]):
            print("#{} {}".format(tc, len(h[0:i])))
            break;
        i = i + 1