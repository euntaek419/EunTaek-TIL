count = 0

T = int(input())
for i in range(T):

    word = list(input())

    for i in range(1, len(word)):
        if(word[i-1] == word[i]):
            word[i-1] = ' '
    
    lenWord = ''.join(word).replace(' ', '')
    word = set(lenWord)

    if(len(lenWord) == len(word)):
        count = count + 1
    
print(count)