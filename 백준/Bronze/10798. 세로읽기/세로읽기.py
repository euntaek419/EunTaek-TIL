data0 = list(input())
data1 = list(input())
data2 = list(input())
data3 = list(input())
data4 = list(input())

dataLength = [len(data0), len(data1), len(data2), len(data3), len(data4)]

result = []

for i in range(0, max(dataLength)):
    if(len(data0) > i):
        result.append(data0[i])
    if(len(data1) > i):
        result.append(data1[i])
    if(len(data2) > i):
        result.append(data2[i])
    if(len(data3) > i):
        result.append(data3[i])
    if(len(data4) > i):
        result.append(data4[i])

print(''.join(result))