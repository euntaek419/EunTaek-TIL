def is_sosu(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    while True:
        if is_sosu(n):
            print(n)
            break
        n += 1
