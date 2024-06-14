word = list(input())

for i in range(0, len(word)):
    if(word[i].isupper() == True):
        word[i] = word[i].lower()
    else:
        word[i] = word[i].upper()

print(''.join(word))