import sys
input = sys.stdin.readline

N,M = map(int, input().split()) #바구니 N개 / M번 실행
B = ['0'] * (N+1) #버킷

for i in range(M):
    a,b,c = map(int, input().split()) #a번 바구니부터 b번 바구니까지 c번호 기입
    for n in range(a, b+1):
        B[n] = str(c)

print(' '.join(B[1:]))