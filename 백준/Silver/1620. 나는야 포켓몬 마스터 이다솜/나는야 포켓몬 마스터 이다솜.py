import sys
input = sys.stdin.readline

n,m = map(int, input().split())

array = {}
array2 = {}

for i in range(1, n+1):
    word = input()
    array[i] = word
    array2[word.strip()] = i

for i in range(m):
    word = input().strip()
    
    if(word.isdigit()):
        print(array[int(word)].strip())
    else:
        print(array2[word])