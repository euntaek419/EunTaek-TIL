array = []

for i in range(0, 5):
    n = int(input())
    array.append(n)

array = sorted(array)

print(sum(array) // 5)
print(array[2])