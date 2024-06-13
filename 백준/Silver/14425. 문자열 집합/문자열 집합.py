# 입력을 빠르게 받기 위해 sys.stdin.read를 사용
import sys
input = sys.stdin.read

# 입력 받기
data = input().split()

# 첫 번째 줄의 두 숫자 N과 M
n = int(data[0])
m = int(data[1])

# N개의 문자열을 집합에 저장
set_s = set(data[2:2+n])

# M개의 문자열을 리스트로 저장
queries = data[2+n:]

# 결과를 저장할 변수
count = 0

# 각 문자열이 집합에 있는지 확인
for query in queries:
    if query in set_s:
        count += 1

# 결과 출력
print(count)