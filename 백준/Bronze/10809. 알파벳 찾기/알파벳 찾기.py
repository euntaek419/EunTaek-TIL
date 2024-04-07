s = list(input())

result = [-1] * 26

for i in range(0, len(s)):
    if(result[ord(s[i])-97] == -1):
        result[ord(s[i])-97] = i

print(' '.join(map(str, result)))