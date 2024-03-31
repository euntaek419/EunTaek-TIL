a = int(input())

a = a // 4
b = []

for i in range(0, a):
    b.append("long")

b.append("int")

print(' '.join(b))