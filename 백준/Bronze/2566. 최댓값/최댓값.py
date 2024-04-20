data = []
count = [0, 0, 0]

for i in range(0, 9):
    data = list(map(int, input().split()))
    if(count[0] < max(data)):
        count[0] = max(data)
        count[1] = i + 1 
        count[2] = data.index(max(data)) + 1

if(str(count[1]) == '0' and str(count[2]) == '0'):
    print(0)
    print(1,1)
else:
    print(count[0])
    print(str(count[1]), str(count[2]))