word = input()

Alpha = ['c=','c-','d-','lj','nj','s=','z=']
Alpha2 = 'dz='

result = 0
alLen = len(word)+1

for i in range(0, alLen):
    if(word[i:i+3] == Alpha2):
        result = result + 1
        word = word[:i] + ' ' + word[i+3:]

alLen = len(word)+1

for i in range(0, len(Alpha)):
    for j in range(0, alLen):
        if(word[j:j+2] == Alpha[i]):
            result = result + 1
            word = word[:j] + ' ' + word[j+2:]

word = word.replace(" ", '')

print(result+len(word))