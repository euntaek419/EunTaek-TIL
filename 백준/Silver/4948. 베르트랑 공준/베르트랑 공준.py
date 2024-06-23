def sieve(max_num):
    is_sosu = [True] * (max_num + 1)
    is_sosu[0] = is_sosu[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if is_sosu[i]:
            for j in range(i*i, max_num + 1, i):
                is_sosu[j] = False
    return is_sosu

is_sosu = sieve(246912)

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(is_sosu[n+1:2*n+1]))