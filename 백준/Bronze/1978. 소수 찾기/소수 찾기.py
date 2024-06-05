n = int(input())

data = list(map(int, input().split()))

result = 0

for i in data:
    count = 0
    for j in range(1,i):
        if( i % j == 0 ):
            count += 1
    
    if(count == 1):
        result += 1

print(result)