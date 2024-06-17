a,b = map(int, input().split())

data = set(map(int, input().split()))
data2 = set(map(int, input().split()))

newdata = data - data2

newdata2 = data2 - data

print(len(newdata) + len(newdata2))