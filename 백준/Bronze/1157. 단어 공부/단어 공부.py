A = input()

A = A.upper()

A = list(A)

dic = {}

for i in range(0, len(A)):
    if( A[i] in dic):
        dic[A[i]] = dic[A[i]] + 1
    else:
        dic[A[i]] = 1

maxValue = max(dic.values())
maxKey = []

for key, value in dic.items():
    if value == maxValue:
        maxKey.append(key)

if(len(maxKey) > 1):
    print('?')
else:
    print(maxKey[0])