T = int(input())

array = []

for i in range(T):
    array.append(input())

array = sorted(set(array), key=lambda x: (len(x), x))

for i in array:
    print(i)