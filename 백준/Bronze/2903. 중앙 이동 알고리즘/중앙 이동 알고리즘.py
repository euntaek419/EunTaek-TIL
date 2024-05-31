n = int(input())

array = [2, 3, 5, 9, 17, 33]

if(n > 5):
    for i in range(5, n):
        array.append(array[i] * 2 - 1)

print(array[n]*array[n])