T = int(input())

array = []

for i in range(T):
    [x,y] = map(int, input().split())
    array.append([x,y])

array = sorted(array)

for i in array:
    print(i[0], i[1])