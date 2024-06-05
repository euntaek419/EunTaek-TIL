data = list(map(int, input().split()))

array = []

array.append(data[0])
array.append(data[1])
array.append(data[2] - data[0])
array.append(data[3] - data[1])

array = sorted(array)

print(array[0])