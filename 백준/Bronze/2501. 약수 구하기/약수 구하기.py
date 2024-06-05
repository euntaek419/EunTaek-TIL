n1, n2 = map(int, input().split())

count = 0
num = 0
for i in range(1, n1+1):
    if(n1 % i == 0):
        count += 1
        if(count == n2):
            num = i

print(num)