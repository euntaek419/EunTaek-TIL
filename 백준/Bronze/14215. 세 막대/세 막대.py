data = list(map(int, input().split()))

data = sorted(data)

while data[0] + data[1] <= data[2]:
    data[2] -= 1

print(sum(data))