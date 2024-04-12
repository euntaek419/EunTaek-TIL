data = list(map(int, input().split()))
count = 0

for i in range(0, len(data)):
    count = count + data[i] * data[i]

print(count % 10)