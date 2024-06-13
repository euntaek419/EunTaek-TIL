def search(array, target, start, end): #이진 탐색
    while start <= end:
        mid = (start + end) // 2 # 중간 인덱스
        if array[mid] == target:
            return True # 찾는 값이 결과와 같으면 리턴
        elif array[mid] > target:
            end = mid - 1 # 중간 값이 찾는 값보다 크면 오른쪽
        else:
            start = mid + 1 # 중간 같이 찾는 값보다 작으면 왼쪽
    return False

n = int(input())
data = list(map(int, input().split()))

data = sorted(data)

m = int(input())
data2 = list(map(int, input().split()))

result = []

for i in data2:
    if search(data, i, 0, n-1):
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))