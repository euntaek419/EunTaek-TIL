T = int(input())

array = []

for i in range(T):
    [x,y] = map(int, input().split())
    array.append([y,x])

array = sorted(array)

for i in array:
    print(i[1], i[0])