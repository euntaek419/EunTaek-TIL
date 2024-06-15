import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

# 첫 번째 리스트의 값들을 카운트
count_dict = Counter(data)

# 두 번째 리스트의 값들이 첫 번째 리스트에 몇 번 등장하는지 확인
result = ' '.join(str(count_dict[i]) if i in count_dict else '0' for i in data2)

print(result)