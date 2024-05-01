T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    word = input()
    newWord = list(word)
    newWord = list(reversed(newWord))
    newWord = ''.join(newWord)
    
    if(newWord == word):
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))