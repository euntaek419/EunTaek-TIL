s = input()
array = set()
length = len(s)

for i in range(length):
    for j in range(i + 1, length + 1):
        array.add(s[i:j])

print(len(array))