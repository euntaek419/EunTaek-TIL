n = int(input())

count = 1

while count < n:
    n -= count
    count += 1

if( count % 2 == 0):
    bunja = n
    bunmo = count - n + 1
else:
    bunja = count - n + 1
    bunmo = n
    
print(str(bunja)+'/'+str(bunmo))