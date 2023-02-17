def solution(slice, n): #피자조각수 slick / 먹는 사람 n
    return ((n-1) // slice) +1 #슬라이스 조각에 딱 맞는 상황을 방지하기 위해 먹는사람 줄였다가 나중에 추가