pieces = list(map(int, input().split()))

target = [1, 1, 2, 2, 2, 8]

result = []

for i in range(len(target)):
    newPiece = target[i] - pieces[i]
    result.append(newPiece)

print(' '.join(map(str, result)))