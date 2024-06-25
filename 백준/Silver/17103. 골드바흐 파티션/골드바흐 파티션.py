import sys
input = sys.stdin.readline

sosu = []
array = [0] * 1000001
array[0] = array[1] = 1

for i in range(2, 1000001):
    if array[i] == 0:
        sosu.append(i)
        for j in range(2*i, 1000001, i):
            array[j] = 1

T = int(input())

for _ in range(T):
    count = 0
    N  = int(input())
    for i in sosu:
        if i >= N:
            break
        if not array[N - i] and i <= N-i:
            count += 1
    print(count)