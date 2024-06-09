n = int(input())

count = 0

while (n % 5 != 0 and n > 0):
    count += 1
    n -= 3

if(n % 5 == 0):
    print(n // 5 +count)
else:
    print(-1)