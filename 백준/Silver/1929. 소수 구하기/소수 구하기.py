def is_sosu(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def sosu(n, m):
    sosus = []
    for num in range(n, m + 1):
        if is_sosu(num):
            sosus.append(num)
    return sosus

n,m = map(int, input().split())

result = sosu(n,m)

for i in result:
    print(i)