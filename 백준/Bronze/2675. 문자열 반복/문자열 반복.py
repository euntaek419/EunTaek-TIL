T = int(input())
for i in range(T):
    A, B = map(str, input().split())
    B = list(B)
    result = []

    for j in range(0, len(B)):
        for k in range(0, int(A)):
            result.append(B[j])

    print(''.join(result))