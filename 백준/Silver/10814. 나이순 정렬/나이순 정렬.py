T = int(input())

array = []

for i in range(T):
    a,b = input().split()
    array.append([int(a), b])

array = sorted(array, key=lambda x : x[0])

for i in array:
    print(i[0],i[1])