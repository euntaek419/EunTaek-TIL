n = int(input())
m = int(input())

array = []

for i in range(n, m+1):
    count = 0
    for j in range(1, i):
        if(i%j == 0):
            count += 1
            if(count > 1):
                break
    if(count == 1):
        array.append(i)


array = sorted(array)

if(len(array) == 0):
    print(-1)
else:
    print(sum(array))
    print(array[0])