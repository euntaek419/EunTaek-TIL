num = 0
count = 0
for i in range(0, 20):
    data = list(map(str, input().split()))
    if(data[2] == 'A+'):
        num = num + 4.5* float(data[1])
        count = count + float(data[1])
    elif(data[2] == 'A0'):
        num = num + 4.0* float(data[1])
        count = count + float(data[1])
    elif(data[2] == 'B+'):
        num = num + 3.5* float(data[1])
        count = count + float(data[1])
    elif(data[2] == 'B0'):
        num = num + 3.0* float(data[1])
        count = count + float(data[1])
    elif(data[2] == 'C+'):
        num = num + 2.5* float(data[1])
        count = count + float(data[1])
    elif(data[2] == 'C0'):
        num = num + 2.0* float(data[1])
        count = count + float(data[1])
    elif(data[2] == 'D+'):
        num = num + 1.5* float(data[1])
        count = count + float(data[1])
    elif(data[2] == 'D0'):
        num = num + 1.0* float(data[1])
        count = count + float(data[1])
    elif(data[2] == 'F'):
        num = num + 0* float(data[1])
        count = count + float(data[1])
        

print(num / count)