T = int(input())

for t in range(1, T + 1):

    n = int(input())

    num = list(map(int, input().split()))

    num = sorted(num)

    print(f'#{t}', *num)