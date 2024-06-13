n = int(input())
data = list(map(int, input().split()))

# data를 정렬하여 중복을 제거한 후 array 생성
D = sorted(set(data))

# 각 숫자의 순위를 저장할 딕셔너리 생성
rank = {value: idx for idx, value in enumerate(D)}

# 원래 data의 각 숫자를 순위로 변환
result = [rank[value] for value in data]

print(' '.join(map(str, result)))