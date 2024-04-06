import sys
input = sys.stdin.readline

M = int(input())
score = list(map(int, input().split()))

maxScore = max(score)

for i in range(0, M):
    score[i] = score[i]/maxScore*100

print(sum(score)/M)